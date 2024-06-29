FROM node:19-alpine

#We copy everything to /app in the virtual file system of the container
COPY package.json /app/
COPY src /app/

#We set the working directory to /app
WORKDIR /app

RUN npm install 


CMD ["node", "server.js"]

#to build this: docker build -t node-app:1.0 ./simple_demo
#to run this: docker run -d -p 3000:3000 node-app:1.0