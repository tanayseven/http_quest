#!/usr/bin/env bash
echo $DOCKER_API_KEY > docker login --username=$USERNAME --password-stdin
docker build --target=prod -t $USERNAME/http_quest . || exit 1
docker push $USERNAME/http_quest
