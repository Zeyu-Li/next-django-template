FROM node:14 as base
WORKDIR /app

# copy dependencies and install
COPY package.json .

COPY yarn.lock .

ADD packages /app/packages/

RUN yarn install

WORKDIR /app/packages/frontend


FROM base as dev
EXPOSE 3000
CMD ["yarn", "run", "start"]

FROM base as int

RUN yarn build

FROM nginx:latest as prod

EXPOSE 80

COPY packages/frontend/nginx.conf /etc/nginx/nginx.conf
COPY --from=int /app/packages/frontend/build/ /var/www/