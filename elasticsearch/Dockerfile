ARG VERSION=7.9.1
FROM docker.elastic.co/elasticsearch/elasticsearch-oss:${VERSION}

ARG ODFE_VERSION=1.10.1.0
USER root
RUN /usr/share/elasticsearch/bin/elasticsearch-plugin install --batch https://d3g5vo6xdbdb9a.cloudfront.net/downloads/elasticsearch-plugins/opendistro-security/opendistro_security-${ODFE_VERSION}.zip
USER elasticsearch
