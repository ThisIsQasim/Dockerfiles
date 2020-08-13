ARG VERSION=7.8.0
FROM docker.elastic.co/kibana/kibana-oss:${VERSION}

ARG ODFE_VERSION=1.9.0.0
RUN /usr/share/kibana/bin/kibana-plugin install https://d3g5vo6xdbdb9a.cloudfront.net/downloads/kibana-plugins/opendistro-security/opendistro_security_kibana_plugin-${ODFE_VERSION}.zip
