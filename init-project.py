#!/usr/bin/env python

PROJECT_NAME_PLACEHOLDER = 'imonir'

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


# initiate project with desired name
projectName =  input('Project Name: ')
print('You entered: ' + str(projectName))

confirmed = input('y/n?: ')
print('confimred: ' + str(confirmed))

if (confirmed == 'y'):
    fileList = [
        './docker-compose.yml',
        './docker-compose.override.yml',
        './docker-compose.production.yml',
        './up.py',
        './down.py',
        './log.py',
        './backend/docker-compose.yml',
        './backend/docker-compose.override.yml',
        './backend/docker-compose.production.yml',
    ]
    for filename in fileList:
        replaceStrInFile(filename, PROJECT_NAME_PLACEHOLDER, projectName)
else:
    print('Ok')

