# fullstack docker container kit 
### Work in Progress 
**updated: sep 1, 2018**

An opnionated boilerplate to start building a full stack web application.

A big thank you to [Docker](https://www.docker.com/) :heart:. 

Long gone are the days of working locally and ftp it to server :crying_cat_face: or directly on the server :grimacing:.
Now most of the dev, test, deploy cycle can be automated.

This is a personal take on removing overhead as much as possible and start working on any project right away and deploy with confidence.
Customizations are kept as simple as possible.

This repository acculumates best of what i've learned so far in this regard.


- Table of Contents
  - [Introduction](#introduction)
  - [Documentation](#documentation)
    - [Folder Structure](#folder-structure)
  - [Quick Start](#quick-start)
  - [Todo](#todo)

## Introduction
This starts [nginx](https://hub.docker.com/_/nginx/), [docker-gen](https://github.com/jwilder/docker-gen) and [letsencrypt-nginx-proxy-companion](https://github.com/JrCs/docker-letsencrypt-nginx-proxy-companion) containers.

**docker-gen** container picks containers from **frontend** and **backend** and generates nginx config.
**nginx** container proxies those containers.
**letsencrypt-nginx-proxy-companion** is only used in production and generates valid SSL certificate from [letsencrypt](https://letsencrypt.org/).

**frontend** and **backend** directories reference seperate respositories(submodule) with docker containers for respective parts of the application.


## Documentation
### Folder Structure
```bash
├── backend # backend project added as submodule in this repo
├── certs # ssl certificates in here
│   ├── letsencrypt # letsencrypt generated
│   ├── local # locally generated using create-local-cert.sh
│   │   ├── create-local-ca.sh
│   │   ├── create-local-cert.sh
│   │   ├── .gitignore # only track bash scripts in here 
├── conf.d # docker volume mounts here
│   ├── .gitgignore
├── frontend # frontend project added as submodule in this repo
├── html # docker volume mounts here
│   ├── .gitgignore
├── scripts # Project operation scripts
│   ├── down.py # stops containers defined in docker-compose files
│   ├── init-project.py # bootstraps by changing config files for this and frontend and backend repo
│   ├── log.py # logs output of **nginx-gen** container
│   ├── up.py # starts containers defined in docker-compose files
│   ├── utils.py  
│   ├── .gitgignore
├── vhost.d # docker volume mounts here
├── .gitmodules # git submodule config
├── docker-compose.override.yml # development configs
├── docker-compose.production.yml # production configs
├── docker-compose.yml # common configs
├── LICENSE
├── nginx.tmpl # downloaded from https://raw.githubusercontent.com/jwilder/docker-gen/master/templates/nginx.tmpl
├── README.md
```

### Quick Start

```bash
# Clone the repository
git clone https://github.com/dostokhan/fullstack-start 
# Go inside the directory
cd fullstack-start

# optionally get latest nginx template file 
curl -o nginx.tmpl https://raw.githubusercontent.com/jwilder/docker-gen/master/templates/nginx.tmpl

# Configurare containers with desired project name.
cd scripts
./init-project.py
# Asks for **Project Name**, **Domain Name**, **Email Address* 
# Updates docker container config files and replaces 'fullstack' with given **Project Name**. i.e. network name
#   1. ./docker-compose.yml
#   2. ./docker-compose.override.yml
#   3. ./docker-compose.production.yml
# Generates local CA and SSL certitificates to be used for local development. local CA should be imported to Chrome to see green on https.
# for production letsencrypt-nginx-proxy-companion container manages SSL certificates from letsencrypt
#   1. ./certs/local/ca.crt
#   2. ./certs/local/ca.key
#   3. ./certs/local/ca.srl
#   4. ./certs/local/local.{domainName}.crt
#   5. ./certs/local/local.{domainName}.key
#   6. ./certs/local/local.{domainName}.srl
#   7. ./certs/local/local.api.{domainName}.crt
#   8. ./certs/local/local.api.{domainName}.key
#   9. ./certs/local/local.api.{domainName}.srl
# Runs init-project.py from frontend and backend to initialize there config files. better documented in their respective repository.

# update /etc/hosts file with 'local.{domainName}' and 'local.api.{domainName}' pointing to 127.0.0.1.

# Start development containers
./up.py
```

## Todo
-  [ ] Update script files to have colored output for better understanding
-  [ ] Better organize scripts and remove redundency
-  [ ] Test this to develop and deploy a demo application

