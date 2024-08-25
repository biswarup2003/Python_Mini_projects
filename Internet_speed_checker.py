from tkinter import *
from tkinter import messagebox
import pyspeedtest

#speed checking function

def test():
    speed = pyspeedtest.SpeedTest("www.google.com")
    download_speed = speed.download()
    formatted_speed = f"{download_speed:.2f}"  # Format the speed to 2 decimal places
    a1 = f"{formatted_speed} Byte Per Second"
    messagebox.showinfo("Your Internet Speed", a1)


root=Tk()
root.title("Internet Speed Checker")
root.config(bg="pink")
root.geometry("500x250")

#componants

label1= Label(root,text="Internet Speed checker",font=("Arial",30,"bold"),bg="lightblue").pack()
button1= Button(root, text="Click!!",font=("Arial",30,"bold"),bg="yellow",height="1",width="10",command=test).pack()


root.mainloop()