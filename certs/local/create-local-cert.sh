#!/usr/bin/env bash
set -eu
org=localhost-ca
# domain1=local.www.imonir.com
# domain2=local.api.imonir.com
domain=local.fullstack.imonir.com

sudo trust anchor --remove ca.crt || true

openssl genpkey -algorithm RSA -out ca.key
openssl req -x509 -key ca.key -out ca.crt \
    -subj "/CN=$org/O=$org"


openssl genpkey -algorithm RSA -out "$domain1".key
openssl req -new -key "$domain1".key -out "$domain1".csr \
    -subj "/CN=$domain1/O=$org"

openssl x509 -req -in "$domain1".csr -days 365 -out "$domain1".crt \
    -CA ca.crt -CAkey ca.key -CAcreateserial \
    -extfile <(cat <<END
basicConstraints = CA:FALSE
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid,issuer
subjectAltName = DNS:$domain1
END
    )

sudo trust anchor ca.crt
