#!/usr/bin/env python

#  import subprocess
from os import system, chdir, path



PROJECT_NAME_PLACEHOLDER = 'fullstack'


# initiate project with desired name
domainName = input('Domain Name (something.something): ')

print('DomainName: ' + str(domainName))
confirmed = input('Confirm y/n?: ')

if (confirmed == 'y'):

    print("\nGenerate SSL certificates for local development")
    # check if local CA already exits ?
    chdir('./volumes/certs/local/')

    if ( not path.isfile('ca.crt') or
        not path.isfile('ca.key') or
        not path.isfile('ca.srl')
        ):
        print('Creating local CA files')
        system('./create-local-ca.sh')
    # create ssl certificate for domainName
    system(f"./create-local-cert.sh local.www.{domainName}")
    system(f"./create-local-cert.sh local.api.{domainName}")
else:
    print('Later then.')
