#!/usr/bin/env python

from subprocess import call
#  import utils
#  , isProduction

#  utils.goToParentDir()
#  runProduction = isProduction()

#  createNetwork = 'docker network ls|grep fullstack > /dev/null || docker network create fullstack'
#  subprocess.check_output(['bash','-c', createNetwork])

#  if runProduction
#      startProxyContainers = 'docker-compose -f docker-compose.yml -f docker-compose.production.yml up -d'
#  else:
startProxyContainers = 'docker-compose -f docker-compose.yml -f docker-compose.override.yml up -d'
call(startProxyContainers.split())

