FROM debian:stable-slim

RUN apt-get update && apt-get install -y dbus

COPY system.conf /etc/dbus-1/system.conf

ENTRYPOINT ["dbus-daemon", "--config-file=/etc/dbus-1/system.conf", "--nosyslog", "--nofork", "--nopidfile"]
