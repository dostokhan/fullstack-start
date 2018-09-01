#!/usr/bin/env python

#  import subprocess
import utils
from os import system, chdir, path

utils.goToParentDir()


PROJECT_NAME_PLACEHOLDER = 'fullstack'
DOCKER_CONFIG_FILES = [
    './docker-compose.yml',
    './docker-compose.override.yml',
    './docker-compose.production.yml',
]


# initiate project with desired name
projectName = input('Project Name: ')
domainName = input('Domain Name (something.something.something): ')
emailAddress = input('Email (for use with letsencrypt): ')

print("\nProjectName: " + str(projectName))
print('DomainName: ' + str(domainName))
print('Email: ' + str(emailAddress))
confirmed = input('Confirm y/n?: ')

if (confirmed == 'y'):

    print("\nChange projectName in docker compose files so containers are named after projectName")
    for filename in DOCKER_CONFIG_FILES:
        utils.replaceStrInFile(filename, PROJECT_NAME_PLACEHOLDER, projectName)

    print("\nGenerate SSL certificates for local development")
    # check if local CA already exits ?
    chdir('./certs/local/')
    if ( not path.isfile('ca.crt') or
        not path.isfile('ca.key') or
        not path.isfile('ca.srl')
        ):
        print('Creating local CA files')
        system('./create-local-ca.sh')
    # create ssl certificate for domainName
    system(f"./create-local-cert.sh local.{domainName}")
    system(f"./create-local-cert.sh local.api.{domainName}")

    # got to project root
    utils.goToParentDir()

    print("\nRun frontend Init script:")
    chdir('./frontend/scripts')
    frontendInitCommand= f"./init-project.py {projectName} {domainName} {emailAddress}"
    system(frontendInitCommand)

    print('\nRun backend Init script');
    chdir('./backend/scripts')
    backendInitCommand= './init-project.py ' + str(projectName) + ' ' + str(domainName)
    system(backendInitCommand)

else:
    print('Later then.')
