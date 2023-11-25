#!/bin/sh
# Add your startup script

# DO NOT DELETE
/start_damon.sh &
/etc/init.d/xinetd start;
sleep infinity;
