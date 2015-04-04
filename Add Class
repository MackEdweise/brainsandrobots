from Command import *

class Add:

  def __init__(self,x,y):
    
    self.x=x
    self.y=y
    self.value=x+y
    self.message="Add {} and {} by latching {}, adding {} to {}. Result is {}".format(x,y,x,x,y,x+y)
    self.pcode=[1,1,1,1,1,1,1,1,1,1]
    self.pcode[x]=0
    self.cncfile="addgrbl"
    
    return
    
  def execute(self):
  
    c=Command(self.pcode,self.message)
    c.interpret(2)
    
    return self.value
  
    
  

  
