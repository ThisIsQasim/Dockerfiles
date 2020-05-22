#!/bin/bash

while true; do
    sleep $(( $INTERVAL - ( $INTERVAL * $JITTER / 100 ) + ( $RANDOM % ( $INTERVAL * 2 * $JITTER / 100 ) ) ))
    /usr/sbin/logrotate -v -s $STATUSFILE /etc/logrotate.conf
done