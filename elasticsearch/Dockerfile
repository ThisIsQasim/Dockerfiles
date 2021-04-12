ARG VERSION=7.10.2
FROM docker.elastic.co/elasticsearch/elasticsearch-oss:${VERSION}

ARG ODFE_PLUGINS="opendistro-security/opendistro-security-1.13.0.0 \
                  opendistro-alerting/opendistro-alerting-1.13.0.0 \
                  opendistro-job-scheduler/opendistro-job-scheduler-1.13.0.0 \
                  opendistro-index-management/opendistro-index-management-1.13.2.0 \
                  opendistro-anomaly-detection/opendistro-anomaly-detection-1.13.0.0 \
                  opendistro-sql/opendistro-sql-1.13.0.0 \
                  opendistro-reports-scheduler/opendistro-reports-scheduler-1.13.0.0 \
                  opendistro-asynchronous-search/opendistro-asynchronous-search-1.13.0.1"

ENV ODFE_URL="https://d3g5vo6xdbdb9a.cloudfront.net/downloads/elasticsearch-plugins"

USER root
SHELL ["/bin/bash","-c"]
RUN ODFE_PLUGINS_ARR=($ODFE_PLUGINS);\
    for i in ${ODFE_PLUGINS_ARR[@]}; \
    do ODFE_URLS="${ODFE_URLS} ${ODFE_URL}/${i}.zip"; done;\
    /usr/share/elasticsearch/bin/elasticsearch-plugin install --batch ${ODFE_URLS} repository-s3 repository-gcs &&\
    \
    sed -i 's/#kibana:/kibana:/g; s/#multitenancy_enabled: true/  multitenancy_enabled: true/g' plugins/opendistro_security/securityconfig/config.yml

SHELL ["/bin/sh", "-c"]
USER elasticsearch
