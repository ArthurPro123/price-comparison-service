FROM node:20-slim

RUN npm install -g npm@9.1.3

ADD package.json .
ADD server.js .

RUN npm install

EXPOSE 8080

CMD [ "npm", "start" ]
