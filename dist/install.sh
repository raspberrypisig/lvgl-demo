#!/usr/bin/env bash

cd /home/pi/Desktop
wget https://github.com/raspberrypisig/lvgl-demo/raw/main/dist/clock.py
wget https://github.com/raspberrypisig/lvgl-demo/raw/main/dist/final3.sh
wget https://github.com/raspberrypisig/lvgl-demo/raw/main/dist/final2.sh
wget -O run.sh https://github.com/raspberrypisig/lvgl-demo/raw/main/dist/run.sh
wget https://github.com/raspberrypisig/lvgl-demo/raw/main/dist/Morganite-Medium-144.bin
chmod +x *.sh
sudo wget -O /usr/share/applications/dawn.desktop https://github.com/raspberrypisig/lvgl-demo/raw/main/dist/dawn.desktop
sudo cp /usr/share/applications/dawn.desktop  /etc/xdg/autostart
cp /usr/share/applications/dawn.desktop  /home/pi/Desktop
sudo wget -O /usr/local/bin/micropython https://github.com/raspberrypisig/lvgl-demo/raw/main/micropython
sudo chmod 755 /usr/local/bin/micropython
mkdir -p /home/pi/lv_micropython/lib/lv_bindings/lib
cd /home/pi/lv_micropython/lib/lv_bindings/lib
wget -O lib.zip https://github.com/raspberrypisig/lvgl-demo/raw/main/dist/lib.zip
unzip lib.zip
rm lib.zip

