# fullstack starter kit 


This is a boilerplate to build a full stack web application using React, Node.js, Express, NextJs, Docker. 
It is also configured with own webpack configuration.

- Table of Contents
  - [Introduction](#introduction)
    - [Development mode](#development-mode)
    - [Production mode](#production-mode)
  - [Quick Start](#quick-start)
  - [Documentation](#documentation)
    - [Folder Structure](#folder-structure)
  - [Todo](#todo)

## Introduction
This starts nginx and docker-gen container which will behave as proxy for containers from 'frontend' and 'backend'.

### Development mode

In the development mode, letsencrypt will use locally generated ssl certificates from ./certs/local directory.
it'll also run 'frontend' and 'backend' container's development mode scripts.

### Production mode

In the production mode, letsencrypt will use letsecrypt provided valid certificate for the domain of the app.
letsencrypt-nginx-proxy-companion container is used for auto generating letsencrypt certificates.
it'll also run 'frontend' and 'backend' container's production mode scripts.
## Quick Start

```bash
# Clone the repository
git clone https://github.com/dostokhan/fullstack-start 
# Go inside the directory
cd fullstack-start

# optionally latest nginx template file can be dowloaded
curl -o nginx.tmpl https://raw.githubusercontent.com/jwilder/docker-gen/master/templates/nginx.tmpl

# Configurare containers with desired project name.
python init-project.py
# the project name provided will replace all instance of 'fullstack' from these files
# 1. ./docker-compose.yml
# 2. ./docker-compose.override.yml
# 3. ./docker-compose.production.yml
# 4. ./up.py
# 5. ./down.py
# 6. ./log.py
# 7. ./backend/docker-compose.yml
# 8. ./backend/docker-compose.override.yml
# 9. ./backend/docker-compose.production.yml


# Start development containers
python ./up.py

# Start for production
python ./up.py production

```

## Documentation

### Folder Structure

frontend and backend contains project backend(rest api) and frontend(nextjs based SPA or SSR).

## Introduction
maybe in the future

