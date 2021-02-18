ARG VERSION=7.10.2
FROM docker.elastic.co/kibana/kibana-oss:${VERSION}

ARG ODFE_PLUGINS="opendistro-security/opendistroSecurityKibana-1.13.0.1 \
                  opendistro-alerting/opendistroAlertingKibana-1.13.0.0 \
                  opendistro-anomaly-detection/opendistroAnomalyDetectionKibana-1.13.0.0 \
                  opendistro-query-workbench/opendistroQueryWorkbenchKibana-1.13.0.0 \
                  opendistro-notebooks/opendistroNotebooksKibana-1.13.0.0 \
                  opendistro-reports/linux/x64/opendistroReportsKibana-1.13.0.0-linux-x64 \
                  opendistro-gantt-chart/opendistroGanttChartKibana-1.13.0.0 \
                  opendistro-trace-analytics/opendistroTraceAnalyticsKibana-1.13.0.0-alpha"

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
    echo 'opendistro_security.multitenancy.enabled: true' >> /usr/share/kibana/config/kibana.yml &&\
    echo 'opendistro_security.multitenancy.tenants.enable_global: true' >> /usr/share/kibana/config/kibana.yml &&\
    echo 'opendistro_security.multitenancy.tenants.enable_private: true' >> /usr/share/kibana/config/kibana.yml &&\
    echo 'opendistro_security.multitenancy.tenants.preferred: ["Private", "Global"]' >> /usr/share/kibana/config/kibana.yml &&\
    echo 'opendistro_security.multitenancy.enable_filter: false' >> /usr/share/kibana/config/kibana.yml

SHELL ["/bin/sh", "-c"]