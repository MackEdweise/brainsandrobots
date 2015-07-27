from Command import *
from Add import *
from Compare import *

class Divide:

  def __init__(self,x,y):
    
    self.y=int(y)
    self.x=int(x)
    self.value=self.x//self.y
    self.pcode=[]
    self.cncfile="dividegrbl"
    
    return
    
  def execute(self):
    
    y=self.y
    x=self.x
    s=y
    r=0
    while s<x:
        a=Add(s,y)
        c=Command(a.pcode,a.message)
        c.interpret(2)
      
        b=Compare(s,x)
        d=Command(b.pcode,b.message)
        d.interpret(2)
        self.pcode.append(b.pcode)
        self.message=self.message+b.message
        r+=1
      
        self.message="Add one to count, yielding {}".format(r)
      
        p=Add(r,0)      #To display the count r
        e=Command(p.pcode,self.message)
        e.interpret(2)
    
    
        s=a.value
    
    return self.value
