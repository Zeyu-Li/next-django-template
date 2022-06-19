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