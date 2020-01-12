import tkinter
from tkinter import*
from tkinter import messagebox
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT)
root= Tk()
root.geometry("400x400")
root.title("Test Python GUI")
def LED_ON():
    GPIO.output(14,True)
def LED_OFF():
    GPIO.output(14,False)
def EXIT():
    GPIO.output(14,False)
    ex = messagebox.askquestion("Exit","Exit?")
    if(ex == 'yes'):
        GPIO.cleanup()
        root.destroy()
label = Label(root,text="On-Off light Control" ,pady=5)
label.grid(row=0 , column=0 ,columnspan =3 )
lable_1 = Label(root,text="LED RED : ")
lable_1.grid(row = 1 , column=0 , sticky=E)
button = Button(root, text="ON" , width=10 , pady=3,command = LED_ON)
button.grid(row=1 , column=1 ,sticky=W)
button2 = Button(root, text="OFF" ,width=10 , pady=3, command = LED_OFF)
button2.grid(row = 1 ,column=2 , sticky=W)
button3 = Button(root, text="EXIT" , width=10 , pady=3, command = EXIT)
button3.grid(row = 3 , column=2 , sticky=W)

root.mainloop()
