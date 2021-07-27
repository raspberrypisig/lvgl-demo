#---------------------------------------------------------------------------------------------------------------------
# A dawn clock utitlising the following technologies: raspbian desktop, lvgl, micropython, linux framebuffer
# Issues: screen resolution, date/time from network or RTC, how to set reminders

'''
How to install from scratch:

1. Install Raspberry Pi Desktop to SD card.
2. Follow build instructions from here https://github.com/lvgl/lv_micropython#build-instructions
   It will take a while, at the end you will have ~/lv_micropython/port/unix/micropython

  * One caveat, before doing build, you need to enable the font used in this script. The file to be modified is called  
    ~/lv_micropython/lib/lv_bindings/lv_conf.h

   you will need to change 
   #define LV_FONT_MONTSERRAT_48    0

   to 
   #define LV_FONT_MONTSERRAT_48    1

   To the same for the other montserrat font sizes.


3. To run this program, open a virtual console (Ctrl+Alt+F1), login as pi:raspberry, and run
   /home/pi/lv_micropython/port/unix/micropython /home/pi/clock.py


4. To exit script, press Ctrl-C. To return to Desktop, press Alt+F7

'''
#----------------------------------------------------------------------------------------------------------------------

import lvgl as lv
import utime
import fs_driver

#Uncomment one of the following, true means runs on desktop, false means run inside virtual console
#RUN_THIS_PROGRAM_ON_DESKTOP=False
RUN_THIS_PROGRAM_ON_DESKTOP=True

lv.init()
if RUN_THIS_PROGRAM_ON_DESKTOP:
  import SDL
  SDL.init(w=1920, h=1080)
else:
  import fb
  fb.init()

'''
　load the font file from filesystem
　How to convert font files refer here: https://github.com/lvgl/lv_font_conv
　font-PHT-en-20.bin:
　　　lv_font_conv --size 20 --format bin --bpp 1 --font Alibaba-PuHuiTi-Medium.subset.ttf --range 0x20-0x7f --no-compress -o font-PHT-en-20.bin
'''
fs_drv = lv.fs_drv_t()
fs_driver.fs_register(fs_drv, 'S')
myfont_en = lv.font_load("S:./Morganite-Medium-144.bin")

import sys
sys.path.append('') # See: https://github.com/micropython/micropython/issues/6419
script_path = __file__[:__file__.rfind('/')] if __file__.find('/') >= 0 else '.'

def getCurrentDateTime():
  currentDateTime=utime.localtime()
  year,month,day,hour,minute,second,dayOfWeekIndex,a,b = currentDateTime
  daysOfWeek = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
  dayOfWeek = daysOfWeek[dayOfWeekIndex]
  amOrPm = "PM" if hour >=12 else "PM"
  morningOrAfternoon = "AFTERNOON" if hour >= 12 else "MORNING"
  hour = hour if hour <= 12 else hour - 12
  minute = str(minute) if minute >= 10 else "0 " + str(minute)
  currentTime = "{} : {}".format(hour, minute)
  currentDate = "{}/{}/{}".format(day, month, year)
  return dayOfWeek, currentTime, currentDate, amOrPm, morningOrAfternoon

# Register FB or SDL display driver

disp_buf1 = lv.disp_draw_buf_t()
buf1_1 = bytes(1920*10)
disp_buf1.init(buf1_1, None, len(buf1_1)//4)
disp_drv = lv.disp_drv_t()
disp_drv.init()
disp_drv.draw_buf = disp_buf1
if RUN_THIS_PROGRAM_ON_DESKTOP:
  disp_drv.flush_cb = SDL.monitor_flush
else:
  disp_drv.flush_cb = fb.flush

disp_drv.hor_res = 1920
disp_drv.ver_res = 1080
disp_drv.register()

# Create a screen and set background color to black
mystyle1 = lv.style_t()
mystyle1.set_bg_color(lv.color_hex3(0x000)) 
scr = lv.obj()
scr.add_style(mystyle1, lv.PART.MAIN)


#myfont_en = lv.font_load("./font-PHT-en-20.bin")

#
mystyle2 = lv.style_t()
#mystyle2.set_text_font(myfont_en)
mystyle2.set_text_font(lv.font_montserrat_48)
#mystyle2.set_text_color(lv.palette_main(lv.PALETTE.BLUE))
mystyle2.set_text_color(lv.color_hex3(0xFFF))


mystyle3 = lv.style_t()
mystyle3.set_text_font(lv.font_montserrat_32)
mystyle3.set_text_color(lv.color_hex3(0xFFF))




dayOfWeek, currentTime, currentDate, amOrPm, morningOrAfternoon = getCurrentDateTime()

label1 = lv.label(scr)
label1.set_text(dayOfWeek)
label1.set_pos(0,230)
label1.set_align(lv.ALIGN.TOP_MID)
label1.add_style(mystyle2, 0)

label2 = lv.label(scr)
label2.set_text(currentTime)
label2.set_pos(0, 350)
label2.set_align(lv.ALIGN.TOP_MID)
label2.add_style(mystyle2, 0)

label3 = lv.label(scr)
label3.set_text(amOrPm)
label3.set_pos(250, 350)
label3.set_align(lv.ALIGN.TOP_MID)
label3.add_style(mystyle2, 0)

label4 = lv.label(scr)
label4.set_text(currentDate)
label4.set_pos(0, 850)
label4.set_align(lv.ALIGN.TOP_MID)
label4.add_style(mystyle3, 0)

label5 = lv.label(scr)
label5.set_text(morningOrAfternoon)
label5.set_style_text_font(myfont_en, 0)
label5.set_pos(0, 700)
label5.set_align(lv.ALIGN.TOP_MID)
label5.add_style(mystyle3, 0)


# Regiser mouse device and crosshair cursor

#mouse = evdev.mouse_indev(scr)

# Load the screen

lv.scr_load(scr)
while True:
  utime.sleep(1)
  currentDateTime=utime.localtime()
  dayOfWeek, currentTime, currentDate, amOrPm, morningOrAfternoon = getCurrentDateTime()
  label2.set_text(currentTime)
  label3.set_text(amOrPm)
  label4.set_text(currentDate)
  label5.set_text(morningOrAfternoon)
  
