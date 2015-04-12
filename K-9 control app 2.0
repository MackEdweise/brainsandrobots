
from tkinter import *
import os
import RPi.GPIO as GPIO
import time

GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setmode(GPIO.BOARD)

GPIO.output(17, 0)
GPIO.output(18, 0)
GPIO.output(22, 0)
GPIO.output(23, 0)
GPIO.output(25, 0)
GPIO.output(27, 0)
GPIO.output(2, 0)
GPIO.output(3, 0)
GPIO.output(4, 0)

class App:
  def __init__(self, master):
    frame = Frame(master,bg="black")
    frame.grid()
    
    self.program=Toplevel(frame)
    self.program.title('Program')
    self.program.withdraw()
    
    var = StringVar()
    self.label=Label(frame,textvariable=var,bg="black",fg="blue")
    var.set("K-9 Control")
    var2 = StringVar()
    self.label2=Label(frame,textvariable=var2,bg="black",fg="orange")
    var2.set("Steering")
    var3 = StringVar()
    self.label3=Label(frame,textvariable=var3,bg="black",fg="purple")
    var3.set("Arm")
    var4 = StringVar()
    self.label4=Label(frame,textvariable=var4,bg="black",fg="green")
    var4.set("Speech")
    
    self.label.grid(row=0,column=1)
    self.label2.grid(row=1,column=2)
    self.label3.grid(row=7,column=2)
    self.label4.grid(row=5,column=2)
    
    self.entry = Entry(frame)
    self.entry.grid(row=6,column=2)
    
    self.button1 = Button(frame, 
                         text="QUIT", fg="red",activebackground="red",bg='black',
                         command=frame.quit)
    self.button1.grid(row=0,column=3)
    self.button2 = Button(frame, 
                         text="left", fg="black",activebackground="orange",width=8,
                         command=self.left)
    self.button2.grid(row=3,column=1)
    self.button3 = Button(frame,
                         text="right", fg="black",activebackground="orange",width=8,
                         command=self.right)
    self.button3.grid(row=3,column=3)
    self.button4 = Button(frame, 
                         text="forward", fg="black",activebackground="orange",width=8,
                         command=self.forward)
    self.button4.grid(row=2,column=2)
    self.button5 = Button(frame,
                         text="180", fg="black",activebackground="orange",width=8,
                         command=self.one_eighty)
    self.button5.grid(row=4,column=2)
    self.button6 = Button(frame,
                         text="say", fg="black",activebackground="green",
                         command=self.say)
    self.button6.grid(row=6,column=1)
    self.button7 = Button(frame, 
                         text="Left", fg="black",activebackground="purple",width=8,
                         command=self.arm_left)
    self.button7.grid(row=9,column=1)
    self.button8 = Button(frame, 
                         text="Up", fg="black",activebackground="purple",width=8,
                         command=self.up)
    self.button8.grid(row=8,column=2)
    self.button9 = Button(frame, 
                         text="Right", fg="black",activebackground="purple",width=8,
                         command=self.arm_right)
    self.button9.grid(row=9,column=3)
    self.button10 = Button(frame, 
                         text="Down", fg="black",activebackground="purple",width=8,
                         command=self.down)
    self.button10.grid(row=10,column=2)
    self.button11 = Button(frame, 
                         text="Clamp", fg="black",activebackground="purple",width=4,
                         command=self.clamp)
    self.button11.grid(row=11,column=1)
    self.button12 = Button(frame, 
                         text="Cable", fg="black",activebackground="purple",width=4,
                         command=self.cable)
    self.button12.grid(row=11,column=3)

    
    return
    
  def say(self):
    
    os.system('espeak "{}"'.format(self.entry.get()))
    
    print(self.entry.get())

    return

  def one_eighty(self):
    
    print("180")

    GPIO.output(25,1)
    time.sleep(6)
    GPIO.output(25,0)
      
    return

  def right(self):
      
    print("right turn")
    
    GPIO.output(27,1)
    time.sleep(3)
    GPIO.output(27,0)
    
    return

  def left(self):
      
    print("left turn")
    
    GPIO.output(25,1)
    time.sleep(3)
    GPIO.output(25,0)
    
    return

  def forward(self):
      
    print("forward")
    
    GPIO.output(25,1)
    time.sleep(3)
    GPIO.output(25,0)
    
    GPIO.output(27,1)
    time.sleep(6)
    GPIO.output(27,0)

    
    return

  def arm_left(self):
      
    print("arm left")
    
    GPIO.output(3,0)
    
    GPIO.output(2,1)
    time.sleep(0.1)
    GPIO.output(2,0)
    time.sleep(0.1)
    
    return

  def arm_right(self):
      
    print("arm right")

    GPIO.output(3,1)
    
    GPIO.output(2,1)
    time.sleep(0.1)
    GPIO.output(2,0)
    time.sleep(0.1)

    return

  def up(self):
      
    print("arm up")

    GPIO.output(22,0)
    
    GPIO.output(2,1)
    time.sleep(0.1)
    GPIO.output(2,0)
    time.sleep(0.1)      

    return

  def down(self):
      
    print("arm down")

    GPIO.output(22,1)
    
    GPIO.output(2,1)
    time.sleep(0.1)
    GPIO.output(2,0)
    time.sleep(0.1)    
      
    return

  def clamp(self):
    
    global c
    
    if c==0:  
        print("clamp")
        c=1
        GPIO.output(4,1)
        time.sleep(5)
        GPIO.output(4,0)
    else:
        print("declamp")
        c=0
        GPIO.output(17,1)
        time.sleep(5)
        GPIO.output(17,0)
        
    return

  def cable(self):
    
    global cable
    
    if cable==0:  
        print("deploy")
        cable=1
        GPIO.output(18,1)
        time.sleep(5)
        GPIO.output(18,0)
        
    else:
        print("retract")
        cable=0
        GPIO.output(23,1)
        time.sleep(5)
        GPIO.output(23,0)        
        
    return
  

global c
global cable
c=0
cable=0

root = Tk()

app = App(root)

root.mainloop()

GPIO.cleanup()
