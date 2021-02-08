ARG VERSION=7.10.0
FROM docker.elastic.co/kibana/kibana-oss:${VERSION}

ARG ODFE_VERSION=opendistroSecurityKibana-1.12.0.0
RUN /usr/share/kibana/bin/kibana-plugin install https://d3g5vo6xdbdb9a.cloudfront.net/downloads/kibana-plugins/opendistro-security/${ODFE_VERSION}.zip &&\
    echo 'opendistro_security.cookie.secure: true' >> /usr/share/kibana/config/kibana.yml &&\
    echo 'opendistro_security.cookie.password: ${KIBANA_COOKIE_PWD}' >> /usr/share/kibana/config/kibana.yml
