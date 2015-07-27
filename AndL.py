from Command import *
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.output(24, 0)

class AndL:

  def __int__(self,x):
    
    self.x=x
    self.value=x
    self.message="Set {} as and gate left operand".format(x)
    self.pcode=[1,0,1,1,1,1,1,1,1,1]
    self.cncfile="andlgrbl"
    
    return
  
  def execute(self):
  
    c=Command(self.pcode,self.message)
    c.interpret(2)
    
    return self.value
