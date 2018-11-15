#!/usr/bin/env python

import sys


isProduction = len(sys.argv) > 1  and sys.argv[1] == 'production'
email= 'imonir.com@gmail.com'

# ENV VARIABLES
nodeEnv = 'production' if isProduction else 'development'

# host names
virtualHostQuickgun = 'quickgun.fullstack.imonir.com' if isProduction else 'local.quickgun.fullstack.imonir.com'



quickgunEnv = f"NODE_ENV={nodeEnv}\n"\
  f"VIRTUAL_HOST={virtualHostQuickgun}\n"

if isProduction:
  print(f"Production Config\n")

  quickgunEnv += f"\n"\
    f"LETSENCRYPT_HOST={virtualHostQuickgun}\n"\
    f"LETSENCRYPT_EMAIL={email}\n"



# BACK
with open('./quickgun/.env', 'w+') as f:
    print('Creating ./quickgun/.env')
    f.write(quickgunEnv)
