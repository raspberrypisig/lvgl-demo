#!/usr/bin/env bash

cd /home/pi/Desktop
wget https://github.com/raspberrypisig/lvgl-demo/raw/main/clock.py
wget https://github.com/raspberrypisig/lvgl-demo/raw/main/final3.sh
wget https://github.com/raspberrypisig/lvgl-demo/raw/main/final2.sh
wget -O run.sh https://github.com/raspberrypisig/lvgl-demo/raw/main/runrelease.sh
wget https://github.com/raspberrypisig/lvgl-demo/raw/main/Morganite-Medium-144.bin
chmod +x *.sh
sudo wget -O /usr/share/applications/dawn.desktop https://github.com/raspberrypisig/lvgl-demo/raw/main/dawn.desktop
sudo cp /usr/share/applications/dawn.desktop  /etc/xdg/autostart
cp /usr/share/applications/dawn.desktop  /home/pi/Desktop
sudo wget -O /usr/local/bin/micropython https://github.com/raspberrypisig/lvgl-demo/raw/main/micropython
sudo chmod 755 /usr/local/bin/micropyth
mkdir /home/pi/lv_micropython/lib/lv_bindings/lib
cd /home/pi/lv_micropython/lib/lv_bindings/lib
wget -O lib.zip https://github.com/raspberrypisig/lvgl-demo/raw/main/lib.zip
unzip lib.zip
rm lib.zip

