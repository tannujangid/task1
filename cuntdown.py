from threading import Timer
import time
import tkinter as tk
from tkinter import *
from datetime import datetime
window = Tk()
window.geometry('600x600')#giving size
window.title('PythonGeeks')#giving title
head=Label(window, text="Countdown Clock and Timer", font=('Calibri 15'))# a label
head.pack(pady=20)
Label(window,text="Enter time in HH:MM:SS",font=('bold')).pack()
Entry(window,textvariable = hour,width=30).pack()
Entry(window,textvariable = minus,width=30).pack()
Entry(window,textvariable = secon,width=30).pack()
 
Checkbutton(text='Check for Music',onvalue=True,variable=check).pack()#creating checkbox
 
Button(window,text="Set Countdown",command=countdown,bg='yellow').place(x=260,y=230)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
Label(window,text=current_time).pack()