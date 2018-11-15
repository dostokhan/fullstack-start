#!/usr/bin/env python


from subprocess import call
import sys

if sys.argv[1] == 'up':
    call(['bash', '-c', 'docker-compose -f docker-compose.yml up -d'])
elif sys.argv[1] == 'down':
    call(['bash', '-c', 'docker-compose -f docker-compose.yml down'])
elif sys.argv[1] == 'log':
    call(['bash', '-c', 'docker-compose -f docker-compose.yml logs --follow fullstack-quickgun'])
elif sys.argv[1] == 'bash':
    call(['bash', '-c', 'docker-compose -f docker-compose.yml exec fullstack-quickgun bash'])
else:
    print('oh snap!')
