FROM debian:buster-slim

RUN export DEBIAN_FRONTEND=noninteractive &&\
    \
    apt-get -q -y update &&\
    apt-get -q -y install curl gnupg2 &&\
    echo 'deb http://download.opensuse.org/repositories/home:/rgerhards/Debian_10/ /' > /etc/apt/sources.list.d/home:rgerhards.list &&\
    curl -fsSL https://download.opensuse.org/repositories/home:rgerhards/Debian_10/Release.key | apt-key add - &&\
    apt-get -q -y remove curl gnupg2 &&\
    apt-get -q -y autoremove &&\
    \
    apt-get -q -y update &&\
    apt-get -q -y install rsyslog rsyslog-kafka &&\
    \
    apt-get -q -y clean &&\
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD ["/usr/sbin/rsyslogd","-n","-i","/var/run/syslogd.pid"]