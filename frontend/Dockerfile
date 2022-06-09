FROM node:14 as base

WORKDIR /app

# copy dependencies and install
COPY frontend/package*.json .

COPY frontend/yarn.lock .

RUN yarn install

FROM base as dev

COPY frontend/ .

RUN yarn build

FROM base as int

CMD ["mv", "out/" "/var/www/"]

EXPOSE 3000

CMD ["yarn", "start"]

# from nginx
FROM nginx:latest as prod

EXPOSE 3333

COPY frontend/nginx.conf /etc/nginx/nginx.conf