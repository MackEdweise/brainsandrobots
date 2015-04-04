from Command import *
from Add import *

class Multiply:

  def __init__(self,x,y):
    
    self.x=x
    self.y=y
    self.value=x*y
    self.pcode=[]
    self.message="Result is {}".format(self.value)
    self.cncfile="multiplygrbl"
    
    return
  
  def execute(self):
    
    x=self.x
    y=self.y
    s=x
    for i in range (y):
        a=Add(s,x)
        c=Command(a.pcode,a.message)
        c.interpret(2)
        s=a.value
    
    d=Command(self.pcode,self.message)
    d.interpret(2)
  
    return self.value
