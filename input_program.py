from translator_functions import *
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.output(24, 0)


#talkg("Hello")

freq_blink(2)

p=input("Problem: ")
print()

result=rec_trans(p)

print()
print("result: {}".format(result))
