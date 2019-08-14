#!/usr/bin/env python3.6

#  from subprocess import call
from pathlib import Path
#  import sys
#  import random
#  import string


PROJECT_NAME = 'fullstack'
ENVIRONMENT = Path('.env.run').read_text().rstrip()

print(f"Environment: {ENVIRONMENT}")
notDevelopment = ENVIRONMENT != 'development'


# CONTAINERS
containerDockergen = 'docker-gen'
containerNginx = 'nginx'

# env vars
logDirectories = '/var/log/docker'
logInterval = 'daily'
logSize = '25M'
logCopies = 10
logDateformat = '%Y-%m-%d'
logAutoupdate = False
timeZone = 'GMT+6'


# docker-gen env file
envDockergen = f"COMPOSE_PROJECT_NAME={PROJECT_NAME}"

# nginx env file
envNginx = f"COMPOSE_PROJECT_NAME={PROJECT_NAME}"

# nginx env file
envLetsencrypt = f"COMPOSE_PROJECT_NAME={PROJECT_NAME}\n"\
      f"NGINX_DOCKER_GEN_CONTAINER={containerDockergen}\n"\
      f"NGINX_PROXY_CONTAINER={containerNginx}"


# logrotate db env file
envLogrotate = f"COMPOSE_PROJECT_NAME={PROJECT_NAME}\n"\
      f"LOGS_DIRECTORIES={logDirectories}\n"\
      f"LOGROTATE_INTERVAL={logInterval}\n"\
      f"LOGROTATE_SIZE={logSize}\n"\
      f"LOGROTATE_COPIES={logCopies}\n"\
      f"LOGROTATE_DATEFORMAT={logDateformat}\n"\
      f"LOGROTATE_AUTOUPDATE={logAutoupdate}"

# rsyslog env file
envRsyslog = f"COMPOSE_PROJECT_NAME={PROJECT_NAME}\n"\
      f"TZ={timeZone}"


# WRITE TO ENV FILES
with open('./.env.dockergen', 'w+') as f:
    print('Creating ./.env.dockergen')
    f.write(envDockergen)

with open('./.env.nginx', 'w+') as f:
    print('Creating ./.env.nginx')
    f.write(envNginx)

with open('./.env.letsencrypt', 'w+') as f:
    print('Creating ./.env.letsencrypt')
    f.write(envLetsencrypt)

with open('./.env.logrotate', 'w+') as f:
    print('Creating ./.env.logrotate')
    f.write(envLogrotate)


with open('./.env.rsyslog', 'w+') as f:
    print('Creating ./.env.rsyslog')
    f.write(envRsyslog)


print("\n")
print('DONE!')
