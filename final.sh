#!/usr/bin/env bash
setsid bash -c 'cd /home/pi/Desktop; exec ./run.sh <> /dev/tty2 >&0 2>&1'
chvt 2
chvt 7
