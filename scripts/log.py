#!/usr/bin/env python

import subprocess
import os

os.chdir('../')


showLog = 'docker-compose logs --follow nginx-gen'

subprocess.call(['bash', '-c', showLog])
