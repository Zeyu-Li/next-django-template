init: hosts env install up

hosts: 
	echo "127.0.0.1       mail.next-django-template.test api.next-django-template.test" | sudo tee -a /etc/hosts

# runs container
up:
	docker-compose up -d
	@echo "To run the backend do \`make run\`"

down:
	docker-compose down

# add frontend library
add-%:
	yarn --cwd frontend/ add $*

run:
	yarn --cwd frontend/ dev

# get docker logs backend
logs:
	docker-compose logs -f backend

# DB migrations
migration:
	cd backend && python3 manage.py makemigrations && python3 manage.py migrate

# DB migrations
named-migration:
	cd backend && python3 manage.py makemigrations -n $(name) && python3 manage.py migrate

# lints frontend
lint:
	yarn --cwd frontend/ lint 

# opens e2e tests
e2e:
	yarn --cwd frontend/ cypress

install:
	yarn --cwd frontend/ install

# sets env
env:
	@test -f .env || cp .env.local .env
# @cp backend/.env.local backend/.env