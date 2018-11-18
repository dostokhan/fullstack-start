#!/usr/bin/env python


from subprocess import call
import sys


branch = sys.argv[1]
environment = sys.argv[2]


print(f"Down environement: {environment}")
call(['python', '-c', f"./run.py down ${branch}"])

print(f"Getting Latest code from {branch}")
call(['bash', '-c', f"git pull origin ${branch}"])
call(['bash', '-c' , 'git submodule update --recursive --remote'])

print(f"Up environment: {environment}")
call(['python', '-c', f"./run.py up ${branch}"])

