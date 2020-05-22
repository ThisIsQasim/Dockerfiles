#!/bin/bash

kill_children()
{
    kill -9 $(jobs -p)
    exit #$
}
trap kill_children SIGINT
trap kill_children SIGTERM
trap kill_children SIGKILL

while true; do
    sleep $(( $INTERVAL - ( $INTERVAL * $JITTER / 100 ) + ( $RANDOM % ( $INTERVAL * 2 * $JITTER / 100 ) ) )) &
    wait
    /usr/sbin/logrotate -v -s $STATUSFILE /etc/logrotate.conf
done