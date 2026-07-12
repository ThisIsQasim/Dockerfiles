FROM debian:stable-slim

RUN apt-get update && \
    apt-get upgrade -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    rsync \
    openssh-client \
    tzdata && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
