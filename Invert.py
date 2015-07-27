from Command import *


class Invert:

  def __init__(self,x):
  
    if x==1:
        self.value=0
    else:
        self.value=1
    
    self.x=x
    self.pcode=[1,1,1,0,1,1,1,1,1,1]
    self.message="Invert current logic value {} to {}".format(x,self.value)
    self.cncfile="invertgrbl"
    
    return
    
  def execute(self):
  
    c=Command(self.pcode,self.message)
    c.interpret(2)
    
    return self.value
