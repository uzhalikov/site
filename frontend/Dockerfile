FROM node:alpine AS build

WORKDIR /site

COPY package.json package.json
RUN npm install
COPY . .
RUN npm run build