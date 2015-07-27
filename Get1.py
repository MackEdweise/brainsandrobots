from Command import *
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.output(24, 0)

class Get1:
  
  def __init__(self):
  
    self.value=1
    self.pcode=[0,1,1,1,1,1,1,1,1,1]
    self.message="Set current working value as one"
    self.cncfile="get1grbl"
    
    return
  
  def execute(self):
  
    c=Command(self.pcode,self.message)
    c.interpret(2)
    
    return self.value
