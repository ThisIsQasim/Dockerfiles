ARG VERSION=7.10.0
FROM docker.elastic.co/kibana/kibana-oss:${VERSION}

ARG ODFE_PLUGINS="opendistro-security/opendistroSecurityKibana-1.12.0.0 \
    opendistro-alerting/opendistroAlertingKibana-1.12.0.2 \
    opendistro-anomaly-detection/opendistroAnomalyDetectionKibana-1.12.0.0 \
    opendistro-query-workbench/opendistroQueryWorkbenchKibana-1.12.0.0 \
    opendistro-notebooks/opendistroNotebooksKibana-1.12.0.0 \
    opendistro-reports/linux/x64/opendistroReportsKibana-1.12.0.0"

ENV ODFE_URL="https://d3g5vo6xdbdb9a.cloudfront.net/downloads/kibana-plugins"

SHELL ["/bin/bash","-c"]
RUN ODFE_PLUGINS_ARR=($ODFE_PLUGINS);\
    for i in ${ODFE_PLUGINS_ARR[@]}; \
    do\
        /usr/share/kibana/bin/kibana-plugin install ${ODFE_URL}/${i}.zip;\
    done;\
    \
    echo 'opendistro_security.cookie.secure: true' >> /usr/share/kibana/config/kibana.yml &&\
    echo 'opendistro_security.cookie.password: ${KIBANA_COOKIE_PWD}' >> /usr/share/kibana/config/kibana.yml &&\
    echo 'opendistro_security.multitenancy.enabled: false' >> /usr/share/kibana/config/kibana.yml

SHELL ["/bin/sh", "-c"]