# Docker Proxy Container with Letsencrypt

- Table of Contents
  - [Introduction](#introduction)
  - [Documentation](#documentation)
    - [Folder Structure](#folder-structure)
  - [Quick Start](#quick-start)

## Introduction
This starts [nginx](https://hub.docker.com/_/nginx/), [docker-gen](https://github.com/jwilder/docker-gen) and [letsencrypt-nginx-proxy-companion](https://github.com/JrCs/docker-letsencrypt-nginx-proxy-companion) containers.

**letsencrypt-nginx-proxy-companion** is only used in non local environmens to generates valid SSL certificate from [letsencrypt](https://letsencrypt.org/).



## Documentation
### Folder Structure
```bash
├── volumes                         # all folders inside this are mounted in docker container
│   ├── certs                       # ssl certificates in here
│   │  ├── letsencrypt              # letsencrypt generated ssl certificates 
│   │  ├──local                     # locally generated using create-local-cert.sh
│   │     ├── create-local-ca.sh    # creates a CA for local dev cerficiates
│   │     ├── create-local-cert.sh  # creates self signed cerficates for development
│   │     ├── .gitignore            # only track bash scripts in here 
│   ├── conf.d
│   │   ├── .gitgignore
│   ├── html
│   │   ├── .gitgignore
│   ├── vhost.d
│   │   ├── .gitgignore
│   ├── templates
│   │   ├── ngnx.tmpl               # downloaded from https://raw.githubusercontent.com/jwilder/docker-gen/master/templates/nginx.tmpl
├── run.py                          # to start, stop, log proxy containers
├── docker-compose.override.yml     # development config
├── docker-compose.production.yml   # production config
├── docker-compose.yml              # common config
├── README.md
```

## Quick Start

```bash
# create **fullstack** network
docker network create fullstack

# optionally get latest nginx template file. Need testing. Latest template can break setup
curl -o nginx.tmpl https://raw.githubusercontent.com/jwilder/docker-gen/master/templates/nginx.tmpl

# create local certificates for development
# Should work on unix like operating systems.
./initialize.py
# Asks for **Domain Name**   i.e. 'fullstack.com'. 
# it'll create 2 SSL certificates for 2 domains
# 1. local.www.fullstack.com
# 2. local.api.fullstack.com

# update /etc/hosts file with above domain names pointing to 127.0.0.1.
127.0.0.1  local.www.fullstack.com
127.0.0.1  local.api.fullstack.com


## Start proxy containers. tasks('up', 'down', 'log') environments('local', 'staging', 'production')
# ./run.py [TASK] [ENVIRONMENT]
./run.py up local

# check if containers are running
docker ps
# should show two containers named **nginx** and **docker-gen** for 'local' environement
```
