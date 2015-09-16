import os
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

GPIO.output(2, 1)
GPIO.output(3, 1)
GPIO.output(4, 1)
GPIO.output(17,1)

GPIO.output(2,1)
time.sleep(0.1)
GPIO.output(2,0)
time.sleep(0.1)


GPIO.cleanup()

