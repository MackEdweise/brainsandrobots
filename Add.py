from Command import *
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.output(24, 0)

class Add:

  def __init__(self,x,y):
    
    self.x=int(x)
    self.y=int(y)
    self.value=self.x+self.y
    self.message="Add {} and {} by latching {}, sending {} and {} to adder chip simultaneosly. Result is {}".format(x,y,x,x,y,self.x+self.y)
    self.pcode=[1,1,1,1,1,1,1,1,1,1]
    self.pcode[self.x]=0
    self.cncfile="addgrbl"
    
    return
    
  def execute(self):
  
    c=Command(self.pcode,self.message)
    c.interpret(2)
    
    return self.value
  
    
  

  
