
from tkinter import *
import os
import tkinter.font as font

import time

window = Tk()
window.geometry("1920x1080")
window.title("玉乳业")

def password():
    os.startfile("prototype.py")
    window.destroy()
    os.startfile("中国第一\中国第一.wav")

myFont = font.Font(family='Helvetica')
myFont = font.Font(size=30)

butt = Button(window, text= "Hi jade welcome back ",command=password, font=('MS Serif,', '100'))
butt.place(relx=.5, rely=.4, anchor="center",)


icon = PhotoImage(file=r"images/diary.gif")

window.iconphoto(True,icon)
window.config(background="#2e5433")

butt.config(background="#2e5433")

window.mainloop()


