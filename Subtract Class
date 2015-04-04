from Command import *
from Add import *
from GetAnd import *
from AndL import *
from AndR import *
from Compare import *

class Subtract:
  
    def __init__(self,x,y):
        
        self.y=y
        self.x=x
        self.value=x-y
        self.pcode=[]
        self.message="Result is {}".format(self.value)
        self.cncfile="subtractgrbl"
      
        return
    
    def execute(self):
        
        y=self.y
        x=self.x
        i=0
        a=Add(i,y)
        while a.value!=x:
            a=Add(i,y)
            c=Command(a.pcode,a.message)
            c.interpret(2)
            COMP=Compare(x,a.value-1)
            d=Command(COMP.pcode,COMP.message)
            d.interpret(2)
            A=AndL()
            AND=Command(A.pcode,A.message)
            AND.interpret(2)
            A2=AndR()
            and2=Command(A2.pcode,A2.message)
            and2.interpret(2)
            GA=GetAnd()
            ga=Command(GA.pcode,GA.message)
            ga.interpret(2)
            i+=1
          
        e=Command(self.pcode,self.message)
        e.interpret(2)
        
        return self.value
