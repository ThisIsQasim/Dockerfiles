ARG VERSION=7.9.1
FROM docker.elastic.co/kibana/kibana-oss:${VERSION}

ARG ODFE_VERSION=1.11.0.0
RUN /usr/share/kibana/bin/kibana-plugin install https://d3g5vo6xdbdb9a.cloudfront.net/downloads/kibana-plugins/opendistro-security/opendistro_security_kibana_plugin-${ODFE_VERSION}.zip &&\
    echo 'opendistro_security.cookie.secure: true' >> /usr/share/kibana/config/kibana.yml &&\
    echo 'opendistro_security.cookie.password: ${KIBANA_COOKIE_PWD}' >> /usr/share/kibana/config/kibana.yml
