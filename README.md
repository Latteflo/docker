# Docker

This repository contains notes and resources on Docker colected along my learning journey.

---

Contents:

- [Docker](#docker)
    - [1. Introduction to Docker](#1-introduction-to-docker)
      - [What is Docker?](#what-is-docker)
      - [Why Use Docker?](#why-use-docker)
    - [2. Docker Architecture](#2-docker-architecture)
      - [Key Components:](#key-components)
    - [3. Basic Docker Commands](#3-basic-docker-commands)
      - [Pulling an Image](#pulling-an-image)
      - [Running a Container](#running-a-container)
      - [Listing Containers](#listing-containers)
      - [Stopping and Removing Containers](#stopping-and-removing-containers)
    - [4. Building Docker Images](#4-building-docker-images)
      - [Dockerfile Basics](#dockerfile-basics)
      - [Building an Image](#building-an-image)
      - [Running Your Image](#running-your-image)
    - [5. Docker Volumes](#5-docker-volumes)
      - [What are Volumes?](#what-are-volumes)
      - [Creating a Volume](#creating-a-volume)
      - [Using a Volume](#using-a-volume)
    - [6. Docker Networking](#6-docker-networking)
      - [Types of Networks](#types-of-networks)
      - [Creating a Network](#creating-a-network)
      - [Connecting a Container to a Network](#connecting-a-container-to-a-network)
    - [7. Docker Compose](#7-docker-compose)
      - [What is Docker Compose?](#what-is-docker-compose)
      - [Example `docker-compose.yml`:](#example-docker-composeyml)
      - [Running Docker Compose](#running-docker-compose)
    - [8. Best Practices](#8-best-practices)
    - [9. Useful Resources](#9-useful-resources)
    - [10. Docker Registries](#10-docker-registries)
    - [Summary](#summary)

---

Repository Structure:

- Simple Demo : Contains a simple Node.js application and a Dockerfile to build a Docker image.
- Python Demo: Contains a simple Python application and a Dockerfile to build a Docker image.
- [Monitoring Demo with Prometheus and Grafana](monitoring_prometeus_grafana/dpg.md): Contains a `docker-compose.yml` file to run the application with Prometheus and Grafana.
- [ElasticSearch Demo with Kibana and Logstash](elk_kibana_logstash/elk.md) : Contains a `docker-compose.yml` file to run the application with ElasticSearch, Kibana and Logstash.
- [SIEM with Suricata and ELK stack](siem_project/siem.md) : Contains a `docker-compose.yml` file to run the application with Suricata and ELK stack.

---

### 1. Introduction to Docker

#### What is Docker?

Docker is a platform that simplifies application deployment by using containers. Containers bundle the application code with all necessary dependencies, ensuring it runs consistently across different environments.

The difference between a **container** and an **image** is that an image is a blueprint for a container, and a container is a running instance of an image.

A running instance of an image is called a container.
An image is a blueprint for a container.
We can run multiple containers from the same image.

#### Why Use Docker?

- **Consistency**: "Works on my machine" problem solved.
- **Isolation**: Keeps applications separate.
- **Efficiency**: Lightweight compared to virtual machines.

---

### 2. Docker Architecture

#### Key Components:

- **Docker Engine**: Core service that runs containers.
- **Images**: Templates for containers.
- **Containers**: Lightweight, standalone, executable packages.
- **Docker Hub**: Cloud-based registry for sharing images.
- **Docker Compose**: Tool for defining and running multi-container applications.

---

### 3. Basic Docker Commands

#### Pulling an Image

Downloads an image from Docker Hub.

```bash
docker pull <image_name>
```

Example: `docker pull ubuntu`

#### Running a Container

Starts a new container from an image.

```bash
docker run <image_name>
```

Example: `docker run ubuntu`

-or we can run a container in detached mode

```bash
docker run -d <image_name>
```

In detached mode if we want to see the logs of the container we can use the following command

```bash
docker logs <container_id>
```

Aplications inside container runs in an isoated Docker network and we need to expose the port of the container to the host machine to access the application running inside the container.

We shall do a port biding.

To expose a port of the container to the host machine we can use the following command

```bash
docker run -d -p <host_port>:<container_port> <image_name>
```

We cannot use the same port for the host machine and the container.

Example: `docker run -d -p 8080:80 nginx`

we can also assign a name to the container using the following command

```bash
docker run -d --name <container_name> -p <host_port>:<container_port> <image_name>
```

Example: `docker run -d --name my-app -p 8080:80 nginx`

#### Listing Containers

Shows all running containers.

```bash
docker ps
```

To see all containers (including stopped):

```bash
docker ps -a
```

#### Stopping and Removing Containers

Stop a running container:

```bash
docker stop <container_id>
```

Remove a container:

```bash
docker rm <container_id>
```

---

### 4. Building Docker Images

Create a Docker image we can use the following command

```bash
docker build -t <image_name> .
```

and -t is used to tag the image with a name.

#### Dockerfile Basics

A `Dockerfile` is a script containing instructions to build a Docker image.

Example `Dockerfile`:

```dockerfile
# Use an official Node.js image
FROM node:14

# Set working directory
WORKDIR /app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy the application code
COPY . .

# Expose a port
EXPOSE 3000

# Command to run the application
CMD ["node", "app.js"]
```

#### Building an Image

Run this command in the directory with your `Dockerfile`:

```bash
docker build -t my-app .
```

#### Running Your Image

```bash
docker run -p 3000:3000 my-app
```

Maps port 3000 of the container to port 3000 on the host.

---

### 5. Docker Volumes

#### What are Volumes?

Volumes allow you to persist data outside the container lifecycle.

#### Creating a Volume

```bash
docker volume create my-volume
```

#### Using a Volume

```bash
docker run -v my-volume:/app/data my-app
```

---

### 6. Docker Networking

#### Types of Networks

- **Bridge**: Default network for containers.
- **Host**: Shares the host network stack.
- **Overlay**: For multi-host networking.

#### Creating a Network

```bash
docker network create my-network
```

#### Connecting a Container to a Network

```bash
docker run --network=my-network my-app
```

---

### 7. Docker Compose

#### What is Docker Compose?

A tool for defining and running multi-container Docker applications using a `docker-compose.yml` file.

#### Example `docker-compose.yml`:

```yaml
version: "3"
services:
  web:
    image: nginx
    ports:
      - "8080:80"
  app:
    build: .
    ports:
      - "3000:3000"
    volumes:
      - my-volume:/app/data
```

#### Running Docker Compose

```bash
docker-compose up
```

To stop:

```bash
docker-compose down
```

---

### 8. Best Practices

- **Keep Images Small**: Use slim base images.
- **Use Multi-stage Builds**: Reduces final image size.
- **Leverage Caching**: Order Dockerfile commands effectively.

---

### 9. Useful Resources

- **Official Documentation**: [Docker Docs](https://docs.docker.com)
- **Docker Hub**: [Docker Hub](https://hub.docker.com)
- **Tutorials**: [Docker Getting Started](https://www.docker.com/get-started)
- **Docker Crash Course**: [TechWorld](https://www.youtube.com/watch?v=pg19Z8LL06w)

### 10. Docker Registries

Dockers registries are services that store and distribute Docker images. The most popular registry is **Docker Hub**, but you can also use private registries like AWS ECR, Google Container Registry, or Azure Container Registry.

There are private and public registries. Docker Hub is a public registry, but you can also create private repositories.

Registry and repository are not the same.

A registry is a service that stores images, and a repository is a collection of related images with the same name.

### Summary

- **Images** are blueprints; **containers** are running instances.
- **Dockerfile** defines how to build an image.
- **Docker Compose** simplifies multi-container applications.
- Volumes and networks help manage data and connectivity.
