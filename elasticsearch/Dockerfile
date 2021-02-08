ARG VERSION=7.10.0
FROM docker.elastic.co/elasticsearch/elasticsearch-oss:${VERSION}

ARG ODFE_VERSION=1.12.0.0
USER root
RUN /usr/share/elasticsearch/bin/elasticsearch-plugin install --batch \
    https://d3g5vo6xdbdb9a.cloudfront.net/downloads/elasticsearch-plugins/opendistro-security/opendistro_security-${ODFE_VERSION}.zip \
    repository-s3 \
    repository-gcs

USER elasticsearch
