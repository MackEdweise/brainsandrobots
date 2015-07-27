from Command import *
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.output(24, 0)

class GetCompare:
  
  def __init__(self,x):
    
    self.x=x
    self.value=x
    self.pcode=[1,1,1,1,1,0,1,1,1,1]
    self.message="Set compare value {} as current working logic value".format(x)
    self.cncfile="getcomparegrbl"
    
    return
    
  def execute(self):
    
    c=Command(self.pcode,self.message)
    c.interpret(2)
    
    return self.value
