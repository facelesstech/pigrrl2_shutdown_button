# shutdown/reboot(/power on) Raspberry Pi with pushbutton
# Button connected to pin 13

import RPi.GPIO as GPIO
from subprocess import call
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def buttonStateChanged(pin):

    if not (GPIO.input(pin)):
        #print"button press"
        #print"Shutdown"
        call(['shutdown', '-h', 'now'], shell=False)

GPIO.add_event_detect(13, GPIO.BOTH, callback=buttonStateChanged)

while True:
    # sleep to reduce unnecessary CPU usage
    time.sleep(5)
