#!/bin/bash
DEFAULTPROJECTS=(onlyoffice samba tastyigniter transmission z-push)
PROJECTS=("${PROJECTS[@]:-${DEFAULTPROJECTS[@]}}")

for PROJECT in ${PROJECTS[@]} ; do
  pwd
  cd $PROJECT
  docker build --pull -t $PROJECT:latest .
  cd ..
  if [[ ! -z $REPO ]]; then
    docker tag $PROJECT:latest $REPO/$PROJECT:latest
    docker push $REPO/$PROJECT:latest
    if cat versions.txt 2> /dev/null | grep $PROJECT; then
      VERSION=$(cat versions.txt | grep $PROJECT | awk '{print $2}')
      docker tag $PROJECT:latest $REPO/$PROJECT:$VERSION
      docker push $REPO/$PROJECT:$VERSION
    fi
  fi
done
