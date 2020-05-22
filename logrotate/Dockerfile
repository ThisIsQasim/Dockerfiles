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
    apt-get -q -y install logrotate curl &&\
    \
    apt-get -q -y clean &&\
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY --from=installer /usr/local/aws-cli/ /usr/local/aws-cli/
COPY --from=installer /aws-cli-bin/ /usr/local/bin/

# The interval between logrotate runs in seconds. And the percentage of random jitter between these runs.
ENV STATUSFILE /var/lib/logrotate/logrotate.status
ENV INTERVAL 3600
ENV JITTER 10

COPY run.sh /logrotated

CMD ["/logrotated"]
