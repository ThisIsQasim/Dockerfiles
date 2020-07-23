FROM debian:buster-slim

RUN export DEBIAN_FRONTEND=noninteractive &&\
    \
    echo 'deb http://ftp.debian.org/debian sid main ' >> /etc/apt/sources.list
    apt-get -q -y update &&\
    apt-get -q -y install rsyslog rsyslog-kafka &&\
    \
    apt-get -q -y clean &&\
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD ["/usr/sbin/rsyslogd","-n","-i","/var/run/syslogd.pid"]