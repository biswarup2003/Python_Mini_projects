#py to exe command : pyinstaller --onefile your_script.py

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import datetime
import getpass
import subprocess
import os

st= Tk()
st.title("Welcome")
st.geometry("400x300")

#fuctions
def username():
    un = getpass.getuser()
    return un

def timeshow():
    current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
    showtime.config(text=current_time)
    showtime.after(1000, timeshow)


def display():
    input = select.get()
    flag = ""
    match(input):
        case('WPS Office'):
            os.startfile(r"\\192.168.5.20\Software\Cmn_Apps_for_all\WPS_NEW.exe")
            flag = True
        case('Microsoft Access'):
            os.startfile(r"\\192.168.5.20\Software\HW_Software\AccessRuntime_X64.exe")
            flag = True
        case('Zoom'):
            os.startfile(r"\\192.168.5.20\hw\Biswarup_Neogi")  
            flag = True
        case('Notepad'):
            os.system('notepad.exe')

        case('ICR(Latest)'):
            os.startfile('https://iimi1.capturedata.com:7553/review/')
            
        case('Dynamic2'):
            os.startfile('https://d-96671daae3.awsapps.com/start/#/?tab=applications')

        case _:
             messagebox.showerror("Input Error", "Select a Valid Option")

    if flag== True:
        sts.config(text= f" Opening {input}...")


#main frame
fr1 = Frame(st)
fr1.pack(pady=10)

# name = Label(fr1, text="First Name:", font=("arial", 15))
# name.grid(row=0, column=0, padx=10, pady=5)
# youwant = Label(fr1, text="Last Name:", font=("arial", 15))
# youwant.grid(row=1, column=0, padx=10, pady=5)

# name = Entry(fr1)
# name.grid(row=0, column=1, padx=10, pady=5)
# youwant = Entry(fr1)
# youwant.grid(row=1, column=1, padx=10, pady=5)

time_label = Label(fr1, text=f"Hello {username()} ", font=("arial", 15))
time_label.pack(pady=10)

showtime = Label(fr1, font=("Helvetica", 25), fg="black")
showtime.pack(pady=10)

# Call timeshow to start updating the time
timeshow()



# Dropdown
fr2 = Frame(st)
fr2.pack(pady=10)
options = ['WPS Office','Microsoft Access','Zoom','Notepad','ICR(Latest)','Dynamic2']
select = ttk.Combobox(fr2, values=options)
select.pack()

submit = Button(fr2, text="Submit", font=("arial", 15), command=display)
submit.pack(pady=10)

sts = Label(fr2, text="Choose an Option", font=("arial", 15)) 
sts.pack(pady=10)



st.mainloop()