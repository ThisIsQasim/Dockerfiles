FROM node:10-slim

RUN npm install --global gitbook-cli &&\
        gitbook fetch &&\
        rm -rf /tmp/*

WORKDIR /srv/gitbook

VOLUME /srv/gitbook /srv/html

EXPOSE 4000 35729

CMD /usr/local/bin/gitbook serve --no-live
