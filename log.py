#!/usr/bin/env python

import subprocess

showLog = 'docker-compose logs --follow nginx-gen-fullstack'

subprocess.call(['bash', '-c', showLog])
