# -- BUILD STEP --

FROM node:20-bullseye AS builder

COPY . /app
WORKDIR /app

RUN npm install --only=production \
    && npm run build
