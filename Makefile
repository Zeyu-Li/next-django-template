# inits docker containers and starts up
init: hosts env install up createsuperuser

# adds proxy aliases
hosts: 
	echo "127.0.0.1       next-django-template.test api.next-django-template.test mail.next-django-template.test" | sudo tee -a /etc/hosts

# runs container
up:
	docker-compose up -d

# brings docker containers down
down:
	docker-compose down

# add frontend library
frontend-add:
	docker-compose exec frontend yarn add $(package)

# add backend library
backend-add:
	echo $(package) >> backend/requirements.txt
	docker-compose exec backend pip3 install $(package)

# add backend app
add-app:
	docker-compose exec backend python3 manage.py startapp $(app)

# add backend app
createsuperuser:
	docker-compose exec backend python3 manage.py createsuperuser --email=admin@admin.com --noinput
# DOESN'T WORK -> docker-compose exec backend cat ./utils/create_superuser.py | python3 backend/manage.py shell
# DOESN'T WORK -> sudo docker exec -it backend python3 manage.py shell < backend/utils/create_superuser.py

# runs frontend locally in dev
# run:
# 	yarn --cwd frontend/ dev

# get docker logs backend
logs-b:
	docker-compose logs -f backend

# get docker logs backend
logs-f:
	docker-compose logs -f frontend

# DB migrations
migration:
	docker-compose exec backend python3 manage.py makemigrations
	docker-compose exec backend python3 manage.py migrate

# DB migrations with a new
named-migration:
	docker-compose exec backend python3 manage.py makemigrations -n $(name)
	docker-compose exec backend python3 manage.py migrate

# lints frontend
lint:
	yarn --cwd frontend/ lint 

test: unit e2e

# backend unit tests
unit:
	python backend/manage.py test backend/ $(ARG) --parallel --keepdb

# opens e2e tests
e2e:
	yarn --cwd frontend/ cypress

# installs frontend dependencies
install:
	yarn --cwd frontend/ install

# will build containers from the ground up
build:
	docker-compose up --build

# sets env
env:
	@test -f .env || cp .env.local .env
# @cp backend/.env.local backend/.env