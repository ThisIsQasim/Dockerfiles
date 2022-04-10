FROM debian:bullseye-slim

RUN apt-get update &&\
    apt-get install -y avahi-daemon &&\
    \
    apt-get -q -y clean &&\
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN sed -i 's/#enable-dbus=yes/enable-dbus=no/g;s/#allow-interfaces=eth0/allow-interfaces=eno1/g;s/use-ipv6=yes/use-ipv6=no/g' /etc/avahi/avahi-daemon.conf 

CMD ["avahi-daemon","--no-chroot","--no-proc-title","-f","/etc/avahi/avahi-daemon.conf"]
