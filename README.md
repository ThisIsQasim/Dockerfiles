# Dockerfiles
A collection of various Dockerfiles in use.

To build multiple docker images at once run
```
PROJECTS="turn samba" ./build.sh 
```
You can also build and push to your own repo by specifying the repo account
```
PROJECTS="turn samba" REPO=dkr.ecr.amazonaws.com ./build.sh
```
