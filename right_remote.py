import time
import RPi.GPIO as GPIO
    
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)
    
GPIO.output(27,1)
time.sleep(3)
GPIO.output(27,0)
    
GPIO.cleanup()
