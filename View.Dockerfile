FROM node:8 as dev
WORKDIR /app
ADD ./view/ /app
RUN export CI=true \
    && yarn install \
    && yarn test
CMD yarn build \
    && yarn start

FROM nginx:1.15 as prod
COPY ./view/build/ /usr/share/nginx/html/
