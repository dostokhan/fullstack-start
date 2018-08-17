#!/usr/bin/env python

import subprocess
import utils

utils.goToParentDir()

showLog = 'docker-compose logs --follow nginx-gen'
subprocess.call(['bash', '-c', showLog])
