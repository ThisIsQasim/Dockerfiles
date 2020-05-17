FROM debian:buster-slim

RUN export DEBIAN_FRONTEND=noninteractive &&\
    \
    apt-get -q -y update &&\
    apt-get -q -y upgrade &&\
    apt-get -q -y install logrotate &&\
    \
    apt-get -q -y clean &&\
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD ["/usr/sbin/logrotate","-v","-s","/var/lib/logrotate/logrotate.status","/etc/logrotate.conf"]
