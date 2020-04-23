#!/bin/sh
https://medium.com/cyberverse/find-secret-api-keys-22cdcc829976
# Compliant
export DANGER_GITHUB_API_TOKEN=
export DANGER_GITHUB_API_TOKEN=""
export DANGER_GITHUB_API_TOKEN=<DANGER_GITHUB_API_TOKEN>
export DANGER_GITHUB_API_TOKEN=$token
export DANGER_GITHUB_API_TOKEN="${token}"
docker run -it -e DRONE_TOKEN=<DRONE_TOKEN> -e DRONE_ID=<ID> image
curl -u admin: https://localhost
curl --user admin:      https://localhost
curl --tlspassword https://localhost
wget --user=admin --ask-password https://localhost
wget --user=admin --password= https://localhost

# Noncompliant
export DANGER_GITHUB_API_TOKEN=YXNkZmZmZmZm_HARDcoded
export DANGER_GITHUB_API_TOKEN="YXNkZmZmZmZm_HARDcoded"
docker run -it -e DRONE_TOKEN="YXNkZmZmZmZm_HARDcoded" -e DRONE_ID=1 image
docker run -it \
    -e DRONE_TOKEN=YXNkZmZmZmZm_HARDcoded \
    -e DRONE_ID=1 \
    image
curl --digest -u admin:YXNkZmZmZmZm_HARDcoded https://localhost
curl --user admin:YXNkZmZmZmZm_HARDcoded https://localhost
curl -k -v \
    --proxy-user admin:YXNkZmZmZmZm_HARDcoded \
    --proxy https://localhost:8080 \
    https://localhost
curl --tlspassword YXNkZmZmZmZm_HARDcoded https://localhost
curl --proxy-tlspassword YXNkZmZmZmZm_HARDcoded https://localhost
wget --password=YXNkZmZmZmZm_HARDcoded https://localhost
wget --http-password=YXNkZmZmZmZm_HARDcoded https://localhost
wget --proxy-password=YXNkZmZmZmZm_HARDcoded https://localhost
wget --ftp-password=YXNkZmZmZmZm_HARDcoded https://localhost