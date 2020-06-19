#!/bin/bash

docker system prune -f

docker images --no-trunc | awk '{ print $3 }' \
    | xargs -r docker rmi --force 2> /dev/nulli

docker ps --filter status=dead --filter status=exited -aq \
  | xargs docker rm -v 2> /dev/null

docker volume ls -qf dangling=true | xargs -r docker volume rm

truncate -s 1000 /var/lib/docker/containers/*/*-json.log
