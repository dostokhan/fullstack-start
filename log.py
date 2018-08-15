#!/usr/bin/env python

import subprocess

showLog = 'docker-compose logs --follow nginx-gen'

subprocess.call(['bash', '-c', showLog])
