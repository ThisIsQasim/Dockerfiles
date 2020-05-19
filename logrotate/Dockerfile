FROM debian:buster-slim as installer
RUN export DEBIAN_FRONTEND=noninteractive &&\
    \
    apt-get -q -y update &&\
    apt-get -q -y install curl unzip

RUN curl -LO "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" &&\
    unzip awscli-exe-linux-x86_64.zip &&\
    ./aws/install --bin-dir /aws-cli-bin/
    
FROM debian:buster-slim

RUN export DEBIAN_FRONTEND=noninteractive &&\
    \
    apt-get -q -y update &&\
    apt-get -q -y upgrade &&\
    apt-get -q -y install logrotate &&\
    \
    apt-get -q -y clean &&\
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY --from=installer /usr/local/aws-cli/ /usr/local/aws-cli/
COPY --from=installer /aws-cli-bin/ /usr/local/bin/

CMD ["/usr/sbin/logrotate","-v","-s","/var/lib/logrotate/logrotate.status","/etc/logrotate.conf"]
