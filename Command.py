import os
import time
import RPi.GPIO as GPIO
GPIO.setup(24, GPIO.OUT)
GPIO.setmode(GPIO.BOARD)
GPIO.output(24, 0)

class Command:

        def __init__(self,code,message):

            self._code=code

            self._message=message

            return
            

        

        def interpret(self,f):

            os.system('espeak "{}"'.format(self._message))

            i=0
    
            while i< len(self._code):

                GPIO.output(24,self._code[i])

                i=i+1

                time.sleep(f)
                
            
            return
