FROM node:8 as dev
WORKDIR /app
ADD ./view/ /app
RUN npm install
CMD ["npm", "start", ""]


FROM nginx:1.15 as prod
ADD ./view/build /usr/share/nginx/html
