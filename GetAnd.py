from Command import *


class GetAnd:

  def __init__(self,x,y):
    
    self.x=x
    self.y=y
    self.value= int(x) and int(y)
    self.pcode=[1,1,1,1,0,1,1,1,1,1]
    self.message="Set and gate output {} to current working logic value".format(self.value)
    self.cncfile="getandgrbl"
    
    return
  
  def execute(self):
    
    c=Command(self.pcode,self.message)
    c.interpret(2)
    
    return self.value
