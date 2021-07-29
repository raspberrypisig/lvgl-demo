#!/usr/bin/env bash
set -x
sudo apt update
sudo apt install -y build-essential libreadline-dev libffi-dev git pkg-config libsdl2-2.0-0 libsdl2-dev
git clone --recurse-submodules https://github.com/lvgl/lv_micropython
cd lv_micropython/
sed -ir 's/LV_FONT_MONTSERRAT_48    1/LV_FONT_MONTSERRAT_48    0/' lib/lv_bindings/lv_conf.h
make -C mpy-cross
make -C ports/unix
cd
wget https://github.com/raspberrypisig/lvgl-demo/raw/main/clock.py
wget https://github.com/raspberrypisig/lvgl-demo/raw/main/final.sh
wget https://github.com/raspberrypisig/lvgl-demo/raw/main/run.sh 
wget https://github.com/raspberrypisig/lvgl-demo/raw/main/Morganite-Medium-144.bin
chmod +x *.sh
