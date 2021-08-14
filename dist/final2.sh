#!/usr/bin/env bash
set -x
echo -e '\033[?25l'
#setsid bash -c 'sudo chvt 1; cd /home/pi/Desktop ; exec ./run.sh <> /dev/tty1 >&0 2>&1'
/home/pi/Desktop/run.sh
#read  < /dev/tty
sudo pkill micropython
sudo chvt 7
#exec ./run.sh <> /dev/tty1 >&0 2>&1
#./run.sh
#sudo chvt 7
#sudo service lightdm restart
