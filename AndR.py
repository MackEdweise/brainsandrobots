from Command import *


class AndR:

  def __init__(self,x):
    
    self.x=x
    self.value=x
    self.pcode=[1,1,0,1,1,1,1,1,1,1]
    self.message="Set {} as and gate right operand".format(x)
    self.cncfile="andrgrbl"
    
    return
    
  def execute(self):
  
    c=Command(self.pcode,self.message)
    c.interpret(2)
    
    return self.value
