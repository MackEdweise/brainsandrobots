import time
import RPi.GPIO as GPIO
    
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
    
GPIO.output(25,1)
time.sleep(3)
GPIO.output(25,0)
    
GPIO.cleanup()
