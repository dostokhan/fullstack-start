#!/usr/bin/env python

from subprocess import call
import utils
#  , isProduction

utils.goToParentDir()
#  runProduction = isProduction()

#  if runProduction
#      print("Production Config")
#      stopProxyContainers = 'docker-compose -f docker-compose.yml -f docker-compose.production.yml down'
#  else:
print("Development Config")
stopProxyContainers = 'docker-compose -f docker-compose.yml -f docker-compose.override.yml down'
call(stopProxyContainers.split())


print('Stopping Backend')
call(['python', './backend/scripts/down.py'])

print('Stopping Frontend')
call(['python', './frontend/scripts/down.py'])

