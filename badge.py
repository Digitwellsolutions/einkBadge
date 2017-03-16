#!/usr/bin/env python

import os
import sys
import re
import time
from commands import *
from papirus import Papirus
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from time import sleep
import RPi.GPIO as GPIO

user = os.getuid()
if user != 0:
    print ("Script needs to be run as  root")
    sys.exit()

# Command line usage
# papirus-buttons

WHITE = 1
BLACK = 0

SW1 = 21
SW2 = 16
SW3 = 20
SW4 = 19
SW5 = 26

#Ensure that the path is the correct location to your project
projectPath = '/home/pi/Documents/MyProjects/Badge/'

def displayimage(papirus, imagename="", partial=0):
    image = Image.open(projectPath + imagename)

    papirus.display(image)
    if partial == 1:
        papirus.partial_update()
    else:
        papirus.update()

def main():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(SW1, GPIO.IN)
    GPIO.setup(SW2, GPIO.IN)
    GPIO.setup(SW3, GPIO.IN)
    GPIO.setup(SW4, GPIO.IN)
    GPIO.setup(SW5, GPIO.IN)

    # Need this to overcome an issue when the script is run from the cron job at startup
    sleep(10)
    
    papirus = Papirus()

    displayimage(papirus, imagename = "hello.bmp")
    
    while True:
        displayimage(papirus, imagename='andrewonly.bmp', partial=1)
        sleep(1)
        displayimage(papirus, imagename='andrewmarshall.bmp',partial=1)
        sleep(3)
        displayimage(papirus, imagename='DSmonochrome.bmp', partial=1)
        sleep(2)
        displayimage(papirus, imagename='mobileapps.bmp',partial=1)
        sleep(2)
        displayimage(papirus, imagename='gadgetstoo.bmp',partial=1)
        sleep(2)
        displayimage(papirus, imagename="hello.bmp")
        sleep(2)

if __name__ == '__main__':
    main()


