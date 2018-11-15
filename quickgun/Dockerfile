# create image based on official node 8 image from Docker
FROM node:8.10

# set environment
ENV NPM_CONFIG_LOGLEVEL warn
# ARG env
# ENV NOTE_ENV $env

# install dependencies first, in a different location for easier app bind mounting for local development
WORKDIR /home
COPY package.json package-lock.json ./
RUN npm install 
ENV PATH /home/node_modules/.bin:$PATH

# check every 30s to ensure this service returns HTTP 200
# HEALTHCHECK --interval=30s CMD node healthcheck.js

# copy in our source code last, as it changes the most
WORKDIR /home/app
COPY . /home/app

# run app
CMD [ -f "/bin/bash" ] && if [ ${NODE_ENV} = production ]; \
  then \
  npm start; \
  else \
  npm start; \
  fi
# npm install; npm start; \

