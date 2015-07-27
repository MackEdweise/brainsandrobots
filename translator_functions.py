import serial
import time
import RPi.GPIO as GPIO
from Add import *
from Command import *
from Divide import *
from Multiply import *
from Subtract import *
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.output(24, 0)


EDGE=8
EDGE2=16
GLOBAL_I=0
GLOBAL_I2=0

def rec_trans(p):
    
    L=[]
    
    reference=None
    
    x=""
    y=""
    
    current_var="x"
    
    index=0
    
    print("problem length: {}".format(len(p)))
    
    while index<len(p):
        
        print()
        print("index: {}".format(index))
        print()
        
        if p[index]=='(' or p[index]=='[' or p[index]=='{':
            
            if p[index]=='(':
                bracket=')'

            if p[index]=='[':
                bracket=']'
        
            if p[index]=='{':
                bracket='}'
                       
            i=index
            while p[i] != bracket:
                i+=1
                
            p2 = p[index+1:i]
            
            if current_var == "x":
                x=rec_trans(p2)
            elif current_var == "y":
                y=rec_trans(p2)        
            
            result,reference,current_var = current_var_switch(L,p,current_var,x,y,index,reference)
            
            index=i+1
        
        elif p[index].isdigit():
            
            if current_var == "x":
                x=x+p[index]
                print("add x")
        
            elif current_var == "y":
                y=y+p[index]
                print("add y")
        
        elif p[index] == " ":
            
            print("space")
            result,reference,current_var = current_var_switch(L,p,current_var,x,y,index,reference)
            
                        
        index+=1
        
    for e in L:
        e.execute()

    global GLOBAL_I
    global GLOBAL_I2
    global EDGE
    global EDGE2
    
    talkg("gotostart")    
    
    for e in L:
        
        for i in e.x:
            if GLOBAL_I==EDGE-1:
                GLOBAL_I=0
                if not GLOBAL_I2==EDGE2-1:
                    talkg("nextline")
                    GLOBAL_I2+=1
                else:
                    talkg("gotostart")
                    GLOBAL_I2=0
            talkg(convert_to_filename(i))
            talkg("nextchar")
            GLOBAL_I+=1
        
        talkg(e.cncfile)
        talkg("nextchar")
        
        for i in e.y:
            if GLOBAL_I==EDGE-1:
                GLOBAL_I=0
                if not GLOBAL_I2==EDGE2-1:
                    talkg("nextline")
                    GLOBAL_I2+=1
                else:
                    talkg("gotostart")
                    GLOBAL_I2=0
            talkg(convert_to_filename(i))
            talkg("nextchar")
            GLOBAL_I+=1
        
        talkg("equals")
        talkg("nextchar")
        
        for i in e.value:
            if GLOBAL_I==EDGE-1:
                GLOBAL_I=0
                if not GLOBAL_I2==EDGE2-1:
                    talkg("nextline")
                    GLOBAL_I2+=1
                else:
                    talkg("gotostart")
                    GLOBAL_I2=0
            talkg(convert_to_filename(i))
            talkg("nextchar")
            GLOBAL_I+=1
        
        talkg("nextline")
        
    return result
                
def current_var_switch(L,p,current_var,x,y,index,ref):
    
    print(current_var)
    
    if current_var == "x":
        print("x: {}".format(x))
        
        current_var = "y"
        ref = index
        result=None
        
    elif current_var == "y":
        print("y: {}".format(y))
        
        search_area = p[ref:index]
        
        if "+" in search_area: 
            result= int(x)+int(y)
            qe=Add(x,y)
            L.append(qe) 
        
        elif "-" in search_area: 
            result= int(x)-int(y)
            qe=Subtract(x,y)
            L.append(qe) 
            
        elif "*" in search_area: 
            result= int(x)*int(y)
            qe=Multiply(x,y)
            L.append(qe) 
            
        elif "/" in search_area: 
            result= int(x)/int(y)
            qe=Divide(x,y)
            L.append(qe) 
            
    return result,ref,current_var

def talkg(file):
    

    s = serial.Serial('/dev/ttyACM0',115200)
     

    f = open(file,'r');
     

    s.write("\r\n\r\n".encode())
    time.sleep(2)   
    s.flushInput()  
     

    for line in f:
        l = line.strip() 
        print ('Sending: ' + l)
        wout = l + '\n'
        s.write(wout.encode()) 
        grbl_out = s.readline() 
        print (' : '.encode() + grbl_out.strip())
     
    next=input(" <Enter> to continue to next sub-problem or finish ")
     
    f.close()
    s.close()
     
def convert_to_filename(num):
    
    if num==0:
        file="zero"
    elif num==1:
        file="one"
    elif num==2:
        file="two"
    elif num==3:
        file="three"
    elif num==4:
        file="four"
    elif num==5:
        file="five"
    elif num==6:
        file="six"
    elif num==7:
        file="seven"
    elif num==8:
        file="eight"
    elif num==9:
        file="nine"
        
    return file

def freq_blink(f):

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(24, GPIO.OUT)

    
    for i in range(4):
        
        GPIO.output(24, 1)
        
        time.sleep(f/2)
    
        GPIO.output(24, 0)
        
        time.sleep(f/2)
    
    GPIO.cleanup()
