FROM debian:buster-slim

RUN export DEBIAN_FRONTEND=noninteractive PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=1 &&\
    apt-get update && apt-get -q -y install curl &&\
    curl -sL https://deb.nodesource.com/setup_14.x | bash - && \
    apt-get -q -y install nodejs &&\
    apt-get -q -y clean &&\
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* &&\
    \
    npm install -g resume-cli jsonresume-theme-elegant &&\
    sed -i~ "s/localhost/0.0.0.0/g" /usr/lib/node_modules/resume-cli/index.js /usr/lib/node_modules/resume-cli/lib/serve.js

WORKDIR /data
ENTRYPOINT ["resume"]
