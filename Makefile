# inits docker containers and starts up
init: hosts env install up

# adds proxy aliases
hosts: 
	echo "127.0.0.1       next-django-template.test api.next-django-template.test mail.next-django-template.test" | sudo tee -a /etc/hosts

# runs container
up:
	docker-compose up -d
	@echo "To run the backend do \`make run\`"

# brings docker containers down
down:
	docker-compose down

# add frontend library
add-%:
	yarn --cwd frontend/ add $*

# runs frontend locally in dev
run:
	yarn --cwd frontend/ dev

# get docker logs backend
logs-b:
	docker-compose logs -f backend

# get docker logs backend
logs-f:
	docker-compose logs -f frontend

# DB migrations
migration:
	cd backend && python3 manage.py makemigrations && python3 manage.py migrate

# DB migrations with a new
named-migration:
	cd backend && python3 manage.py makemigrations -n $(name) && python3 manage.py migrate

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