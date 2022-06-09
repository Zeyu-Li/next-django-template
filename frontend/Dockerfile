FROM node:14 as base

WORKDIR /app

# copy dependencies and install
COPY frontend/package*.json .

COPY frontend/yarn.lock .

COPY frontend .

RUN yarn install

FROM base as dev

EXPOSE 3000

CMD ["yarn", "dev"]

# for prod env
# CMD ["yarn", "start"]

# FROM base as int

# RUN yarn build

# # debug
# # ARG CACHE_TS=default_ts
# # RUN ls -l /app
# # RUN ls -l /

# # from nginx
# FROM nginx:latest as prod

# EXPOSE 3333

# COPY frontend/nginx.conf /etc/nginx/nginx.conf
# COPY --from=int /app/out/ /var/www/