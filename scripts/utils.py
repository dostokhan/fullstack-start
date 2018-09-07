#!/usr/bin/env python

from subprocess import call
import argparse
from os.path import dirname, abspath
from os import chdir, getcwd
from sys import exit

import colors
import constants

def printInfo(message):
    colors.cprint(f"{message}", fg='w', style='b')

def printImportant(message):
    colors.cprint(f"{message}", fg='r', bg='k', style='b')

def printSuccess(message):
    colors.cprint(f"{message}", fg='g', bg='k', style='b')
def printDanger(message):
    colors.cprint(f"{message}", fg='r', bg='w', style='b')

def exitShell():
    colors.cprint('\nSee you later :-)\n', fg='b', style='b')
    exit()


def selectTask():
    print("\n")
    for key, value in constants.TASK_LIST.items():
        print(f"{key} : {value['name']}")

    taskKey = input("Task? : ")
    if taskKey not in constants.TASK_LIST.keys():
        exitShell();

    return constants.TASK_LIST[taskKey]


def selectProject(task, isProduction):
    print("\n")
    #  print(f"task: {task['name']}")
    for key, value in constants.PROJECT_LIST.items():
        print(f"{key} : {value['name']}")

    projectKey = input("Project? : ")
    if projectKey in constants.PROJECT_LIST.keys():
        project = constants.PROJECT_LIST[projectKey]
        printSuccess(f"{task['name']} : {project['name']}")

        if project['action'] == 'frontendbackend':
            doFrontend(task, isProduction)
            doBackend(task, isProduction)
        elif project['action'] == 'frontend':
            doFrontend(task, isProduction)
        elif project['action'] == 'backend':
            doBackend(task, isProduction)
        else:
            exitShell(task)

    else:
        exitShell();

def doFrontend(task, isProduction):
    print('DO FRONTEND');
    scriptFile = f"./frontend/scripts/{task['action']}.py";
    call(['python', scriptFile])

def doBackend(task, isProduction):
    print('DO BACKEND');
    scriptFile = f"./backend/scripts/{task['action']}.py"
    call(['python', scriptFile])

def doProxyContainers(task, isProduction):
    scriptFile = f"./scripts/{task['action']}.py"
    printSuccess(scriptFile)
    call(['python', scriptFile])


def goToParentDir():
    chdir(dirname(dirname(abspath(__file__))))
    print('Current Directory' +  getcwd())


def isProduction():
    parser = argparse.ArgumentParser()
    parser.add_argument("-isProduction", help="Run in Production Config", default="development")
    args = parser.parse_args()

    return args.isProduction == 'production'


def replaceStrInFile(filename, oldString, newString):
    # Safely read the input filename using 'with'
    with open(filename) as f:
        s = f.read()
        if oldString not in s:
            print('"{oldString}" not found in {filename}.'.format(**locals()))
            return

    # Safely write the changed content, if found in the file
    with open(filename, 'w') as f:
        print('Changing "{oldString}" to "{newString}" in {filename}'.format(**locals()))
        s = s.replace(oldString, newString)
        f.write(s)

