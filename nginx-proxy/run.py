#!/usr/bin/env python


from subprocess import call
import sys


if sys.argv[1] == 'up':
    if sys.argv[2] == 'local':
        call(['bash', '-c', 'docker-compose -f docker-compose.yml -f docker-compose.override.yml up -d'])
    else:
        call(['bash', '-c', 'docker-compose -f docker-compose.yml -f docker-compose.production.yml up -d'])
elif sys.argv[1] == 'down':
    if sys.argv[2] == 'local':
        call(['bash', '-c', 'docker-compose -f docker-compose.yml -f docker-compose.override.yml down'])
    else:
        call(['bash', '-c', 'docker-compose -f docker-compose.yml -f docker-compose.production.yml down'])

elif sys.argv[1] == 'log':
    call(['bash', '-c', 'docker-compose logs --follow docker-gen'])
else:
    print('See ya :)')
