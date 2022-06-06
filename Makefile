init: hosts env up

hosts: echo "127.0.0.1       mail.next-django-template.test api.next-django-template.test" | sudo tee -a /etc/hosts

# runs container
up:
	docker-compose up -d
	@echo "To run the backend do \`make run\`"

# lints frontend
lint:
	yarn --cwd frontend/ lint 

# opens e2e tests
test-e2e:
	yarn --cwd frontend/ cypress

# sets env
env:
	@test -f .env || cp .env.example .env
	@cp backend/.env.local backend/.env