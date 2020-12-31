FROM debian:buster-slim

RUN export DEBIAN_FRONTEND=noninteractive PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=1 &&\
    apt-get update && apt-get -q -y install curl &&\
    curl -sL https://deb.nodesource.com/setup_14.x | bash - && \
    apt-get -q -y install nodejs &&\
    apt-get -q -y clean &&\
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* &&\
    \
    PUPPETEER_SKIP_DOWNLOAD=1 \
    npm install -g resume-cli jsonresume-theme-elegant

WORKDIR /data
ENTRYPOINT ["resume"]
