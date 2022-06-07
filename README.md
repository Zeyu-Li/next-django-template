# Next.js-Django Template

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT) [![Support me on GitHub](https://img.shields.io/badge/Support-GitHub-ff69b4)](https://github.com/sponsors/Zeyu-Li)

Boilerplate for a Next.js Django app

## Requirements

- nvm
- node
- yarn
- Docker
- Docker-Compose
- Make
- next
- cypress

### Optional

- pre-commit

## Frontend

Next.js app with BEM SCSS using JS (TS is overkill for frontend and unit tests are meaningless till at least MVP)

![front.png](./front.png)

---

### Dependencies

To add dependencies, `cd frontend` and `yarn add <your_package>` OR `make add-<named-of-pakacage>`

### Development

To run development first install dependencies with `make install` then do `make run`

## Backend

Django backend with logger, email, unit tests

### Migrations

If you change or create model entities, you will need to generate migrations for the DB. Simply run `make migrations` or `make migrations name=migration-name app=app-name` for a named migration where app-name will corresponding to the app where the model was changed. If you do not do this, then your entity changes will not be reflected in the database.

## DevOps

Docker, Docker-compose, Makefiles

To start off do `make init` or do `make up` if you are starting it up again

To bring the services down do `make down`

## Testing

Unit testing for backend and cypress testing for e2e. To run e2e do `make e2e` (unfortunately this does not work on WSL)

## TODOS

Here are a list of things you need to do once you decide to use this template

- change constants in frontend/components/constants/constants for front end defaults
- change .env.local to your personal settings
-

### Support

With inspiration from [github.com/vintasoftware/django-react-boilerplate](https://github.com/vintasoftware/django-react-boilerplate)

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
