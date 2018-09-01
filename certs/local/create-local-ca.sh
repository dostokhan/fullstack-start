#!/usr/bin/env bash
set -eu
org=localhost-ca

sudo trust anchor --remove ca.crt || true

openssl genpkey -algorithm RSA -out ca.key
openssl req -x509 -key ca.key -out ca.crt \
    -subj "/CN=$org/O=$org"

sudo trust anchor ca.crt
