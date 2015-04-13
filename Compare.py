from Command import *
from GetCompare import *

class Compare:
    
  def __init__(self,x,y):  # y would typically be an addition, and x a number.
    
    self.x=x
    self.y=y
    self.value=x>y
    self.message="Compare {} and {}".format(x,y)
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
