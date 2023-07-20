
from tkinter import *
from tkinter import messagebox
from functools import partial
import os
import time
import pyautogui
import webbrowser

window = Tk()
window.geometry("1920x1080")
window.title("玉乳业")

icon = PhotoImage(file=r"images/diary.gif")
window.iconphoto(True,icon)
window.config(background="#2e5433")


def validateLogin():
    print("username entered :", usernameEntry.get())
    print("password entered :", passwordEntry.get())

    username = "jade"
    password = "jade"

    if usernameEntry.get() == username and passwordEntry.get() == password:
        messagebox.showinfo(title="SUCCESFULLY LOGIN", message="WELCOME BACK JADE!!!.")
        webbrowser. open('https://docs.google.com/document/d/1fAbvXhc_e6n8JCFArkCriSw7YzKin-dKZxdDRMqUQWE/edit')
        exit()
        
       
    else:
        messagebox.showerror(title="WHO TF ARE YOU???", message="TERMINATING PROGRAM")
        messagebox.showwarning(title="TERMINATING", message="1")
        messagebox.showwarning(title="TERMINATING", message="2")
        messagebox.showwarning(title="TERMINATING", message="3")
        exit()


username = Label(window, text= "USERNAME",width=10,height=1,
                 font=('Helvetica', '20',), activebackground="#90ee90", background="#C0C0C0",)
usernameEntry = Entry(window, textvariable='username: ', show='*',)


password = Label(window, text= "PASSWORD",width=10,height=1,
                 font=('Helvetica', '20',), activebackground="#90ee90", background="#C0C0C0",)
passwordEntry = Entry(window, textvariable='password: ', show='*')

login = Button(window, text= "LOGIN",width=10,height=1,
                 font=('Helvetica', '20',), activebackground="#90ee90", background="#C0C0C0",command=validateLogin)


validateLogin = partial(validateLogin, username, password)


username.place(relx=.4, rely=.3, anchor="center")
usernameEntry.place(relx=.5, rely=.3, anchor="center", height=30, width=140)

password.place(relx=.4, rely=.4, anchor="center")
passwordEntry.place(relx=.5, rely=.4, anchor="center", height=30, width=140)

login.place(relx=.4, rely=.6, anchor="center")

window.mainloop()

#如果一个中国人遇到这行代码，我感到非常抱歉，我认为这很有趣
#created 6/23/2023
#made by ching chong jade
