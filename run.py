#!/usr/bin/env python

import argparse
from subprocess import call
from sys import path

path.insert(0, './scripts')
import utils



parser = argparse.ArgumentParser()
parser.add_argument("-environment", help="Run in Production Config", default="development")
parser.add_argument("-withproxy", help="Run in Production Config", default="n")
args = parser.parse_args()

isProduction = args.environment == 'production'

utils.printInfo("Environment ?")
utils.printImportant(args.environment);
utils.printInfo("WithProxy ?")
utils.printImportant(args.withproxy);


task = utils.selectTask()


if args.withproxy == 'yes':
    utils.doProxyContainers(task, isProduction)


utils.selectProject(task, isProduction)

