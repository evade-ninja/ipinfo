#!/usr/bin/python3

import netifaces as ni
import RPi.GPIO as GPIO

#from luma import *
import luma
from luma.core import interface
from luma.core import cmdline, error
from luma.core.render import canvas
from luma.oled.device import ssd1331
from PIL import ImageFont

import os
ni.ifaddresses('wlan0')
ip = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
print(ip)

ssid = os.popen("/sbin/iwconfig wlan0 \
                | grep 'ESSID' \
                | awk '{print $4}' \
                | awk -F\\\" '{print $2}'").read()
print(ssid)

GPIO.setwarnings(False)

#device.clear()
serial = luma.core.interface.serial.spi(port=0,device=0)
device = ssd1331(serial_interface=serial,width=96,height=64,persist=True)
device.persist = True

#print(device.persist)i

device.clear()

font1 = ImageFont.truetype(os.path.abspath(os.path.join(os.path.dirname(__file__), "Orbitron-Regular.ttf")), 10)
font2 = ImageFont.truetype(os.path.abspath(os.path.join(os.path.dirname(__file__), "FjallaOne-Regular.ttf")), 11)
font3 = ImageFont.truetype(os.path.abspath(os.path.join(os.path.dirname(__file__), "Oswald-Light.ttf")), 10)

bgcolor = (0,0,128)
if ssid == "" :
	bgcolor = (128,0,0)
elif ip == "" :
	bgcolor = (128,0,0)


with canvas(device) as draw:
	draw.rectangle((0,0,96,64), fill=bgcolor)
	draw.text((2,2), "IP Address", font=font2)
	draw.text((12,16), ip, font=font2)
	draw.text((2,34), "SSID", font=font2)
	draw.text((12,48), ssid, font=font2)
#    draw.text((0,16), "255.255.255.255")

#while 1:
#    print(".")

