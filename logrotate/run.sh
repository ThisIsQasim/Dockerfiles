#!/bin/bash

kill_children()
{
    kill -SIGINT $(jobs -p)
    exit #$
}
trap kill_children SIGINT

while true; do
    sleep $(( $INTERVAL - ( $INTERVAL * $JITTER / 100 ) + ( $RANDOM % ( $INTERVAL * 2 * $JITTER / 100 ) ) )) &
    wait
    /usr/sbin/logrotate -v -s $STATUSFILE /etc/logrotate.conf
done