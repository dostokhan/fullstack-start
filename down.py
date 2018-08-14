#!/usr/bin/env python

import subprocess
import sys
isProduction = sys.argv[1]

#  removeNetwork = 'docker network ls|grep fullstack > /dev/null && docker network rm fullstack'
#  subprocess.check_output(['bash','-c', removeNetwork])

if isProduction == 'production':
    print("Production Config")
    startProxyContainers = 'docker-compose -f docker-compose.yml -f docker-compose.production.yml down -d'
    subprocess.check_output(startProxyContainers.split())
else:
    print("Development Config")
    startProxyContainers = 'docker-compose -f docker-compose.yml -f docker-compose.override.yml down -d'
    subprocess.check_output(startProxyContainers.split())



#  print('Stopping Frontend')
#  import('./frontend/down')

#  echo "Stopping Backend"
#  import ./backend/down

