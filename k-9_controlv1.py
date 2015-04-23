from tkinter import *
import os
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)


class App:
  def __init__(self, master):
    frame = Frame(master,bg="black")
    frame.grid()
    var = StringVar()
    self.label=Label(frame,textvariable=var,bg="black",fg="blue")
    var.set("K-9 Control")
    self.label.grid(row=1,column=1)
    self.entry = Entry(frame)
    self.entry.grid(row=4,column=2)
    self.button1 = Button(frame, 
                         text="QUIT", fg="red",activebackground="red",
                         command=frame.quit)
    self.button1.grid(row=4,column=3)
    self.button2 = Button(frame, 
                         text="left", fg="black",activebackground="orange",width=8,
                         command=self.left)
    self.button2.grid(row=2,column=1)
    self.button3 = Button(frame,
                         text="right", fg="black",activebackground="orange",width=8,
                         command=self.right)
    self.button3.grid(row=2,column=3)
    self.button4 = Button(frame, 
                         text="forward", fg="black",activebackground="orange",width=8,
                         command=self.forward)
    self.button4.grid(row=1,column=2)
    self.button5 = Button(frame,
                         text="180", fg="black",activebackground="orange",width=8,
                         command=self.one_eighty)
    self.button5.grid(row=3,column=2)
    self.button6 = Button(frame,
                         text="say", fg="black",activebackground="green",
                         command=self.say)
    self.button6.grid(row=4,column=1)
    
    return
    
  def say(self):
    
    os.system('espeak "{}"'.format(self.entry.get()))
    
    print(self.entry.get())

    return

  def one_eighty(self):
    
    print("180")

    GPIO.output(22,1)
    time.sleep(6)
    GPIO.output(22,0)
      
    return

  def right(self):
      
    print("right turn")
    
    GPIO.output(23,1)
    time.sleep(3)
    GPIO.output(23,0)
    
    return

  def left(self):
      
    print("left turn")
    
    GPIO.output(22,1)
    time.sleep(3)
    GPIO.output(22,0)
    
    return

  def forward(self):
      
    print("forward")
    
    GPIO.output(22,1)
    time.sleep(3)
    GPIO.output(22,0)
    
    GPIO.output(23,1)
    time.sleep(6)
    GPIO.output(23,0)

    
    return



root = Tk()

app = App(root)

root.mainloop()

GPIO.cleanup()
