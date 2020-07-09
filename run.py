#!/usr/bin/env python3


from subprocess import call
from pathlib import Path
import sys



TASK = sys.argv[1]
ENVIRONMENT = Path('.env.run').read_text().rstrip()
NETWORK = 'fullstack'

CONTAINER = sys.argv[2] if len(sys.argv) > 2 else 'nginx'
COMPOSE_FILES = ' -f docker-compose.yml -f docker-compose.production.yml ' if ENVIRONMENT == 'production' \
    else ' -f docker-compose.yml -f docker-compose.override.yml '

print('ENVIRONMENT: ' + ENVIRONMENT)
print('COMPOSE FILES: ' + COMPOSE_FILES)

def netUp():
    call(['bash', '-c', f"docker network create --subnet=172.28.0.0/16 {NETWORK}"])
def netDown():
    call(['bash', '-c', f"docker network rm {NETWORK}"])

def up():
    call(['bash', '-c', 'docker-compose ' + COMPOSE_FILES + ' up -d '])

def down():
    call(['bash', '-c', 'docker-compose ' + COMPOSE_FILES + ' down'])

def build():
    call(['bash', '-c', 'docker-compose ' + COMPOSE_FILES + ' build '])

def log():
    call(['bash', '-c', f"sudo tail -f ./volumes/log/{CONTAINER}/container.log"])

def bash():
    call(['bash', '-c', f"docker-compose {COMPOSE_FILES} exec {CONTAINER} bash"])

if TASK == 'up':
    netUp()
    up()
elif TASK == 'down':
    down()
    netDown()
elif TASK == 'log':
    log()
elif TASK == 'bash':
    bash()
elif TASK == 'dup':
    down()
    up()
elif TASK == 'bup':
    down()
    build()
    up()
else:
    call(['bash', '-c', 'echo "See ya :)"'])






