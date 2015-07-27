from Command import *
from GetCompare import *
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.output(24, 0)

class Compare:
    
  def __init__(self,x,y):  # y would typically be an addition, and x a number.
    
    self.x=int(x)
    self.y=int(y)
    self.value=self.x>self.y
    self.message="Compare {} and {} by sending them to the comparator simultaneosly".format(x,y)
    self.cncfile="comparegrbl"
    self.pcode=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    self.pcode[x]=0
    self.pcode[y+10]=0
    
    return
  
  def execute(self):
  
    c=Command(self.pcode,self.message)
    c.interpret(2)
    
    gc=GetCompare(self.value)
    gc.interpret(2)
    
    return self.value
