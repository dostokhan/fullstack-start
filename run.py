#!/usr/bin/env python

from subprocess import call
import sys

# argv[1] is task i.e.e up, down etc
# argv[2] is environemnt for tasks(up, down) and container name for tasks(log, bash)


if sys.argv[1] == 'up':
  call(['bash', '-c', f"cd ./nginx-proxy && ./run.py up {sys.argv[2]}"])
  call(['bash', '-c', f"cd ./frontend && ./run.py up"])
  call(['bash', '-c', 'cd ./backend && ./run.py up'])

elif sys.argv[1] == 'down':
  call(['bash', '-c', f"cd ./nginx-proxy && ./run.py down {sys.argv[2]}"])
  call(['bash', '-c', 'cd ./frontend && ./run.py down'])
  call(['bash', '-c', 'cd ./backend && ./run.py down'])

elif sys.argv[1] == 'log':
    call(['bash', '-c', f"cd {sys.argv[2]} && ./run.py log"])

elif sys.argv[1] == 'bash':
    call(['bash', '-c', f"cd {sys.argv[2]} && ./run.py bash"])
else:
    print('See ya :)')
