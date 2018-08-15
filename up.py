#!/usr/bin/env python

import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-isProduction", help="Run in Production Config", default="development")
args = parser.parse_args()

#  createNetwork = 'docker network ls|grep fullstack > /dev/null || docker network create fullstack'
#  subprocess.check_output(['bash','-c', createNetwork])

#  if args.isProduction == 'production':
#      startProxyContainers = 'docker-compose -f docker-compose.yml -f docker-compose.production.yml up -d'
#  else:
startProxyContainers = 'docker-compose -f docker-compose.yml -f docker-compose.override.yml up -d'

subprocess.check_output(['bash', '-c', startProxyContainers])


#  print('Starting Frontend')
#  import ./frontend/up

#  print('Starting Backend')
#  import ./backend/up

