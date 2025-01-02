from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import time
import getpass
import subprocess
import os

st= Tk()
st.title("Welcome")
st.geometry("500x400")

#fuctions
def username():
    un = getpass.getuser()
    return un

def timeshow():
    current_date = time.strftime("%d-%B-%Y")
    current_time = time.strftime("%H:%M:%S")
    text = f"{current_date}\n\n{current_time}"
    showtime.config(text=text)
    showtime.after(1000, timeshow)


def display():
    input = select.get()
    flag = False
    match(input):
        case('Missing Image Processing Excel File'):
            os.startfile(r"C:\Users\3452268\Desktop\New folder\227_PROCESSING.xlsx")
            flag = True
        case('Import Tool'):
            os.startfile(r"C:\Users\3452268\Documents\Biswarup\Import-Tool\Debug\ClientDataImportTool.exe")
            flag = True
        case('My Local server folder'):
            os.startfile(r"\\192.168.5.20\hw\Biswarup_Neogi")  
            flag = True
        case('My local folder'):
            os.startfile(r"C:\Users\3452268\Documents\Biswarup")
            flag= True
        case('RemotePC'):
            subprocess.run('mstsc')
            flag= True
        case('Zoom'):
            os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Zoom\Zoom Workplace.lnk")           
            flag = True
        case('FireFox'):
            os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Firefox.lnk")
            flag= True
        case('D2'):
            url = 'https://d-96671daae3.awsapps.com/start/#/?tab=applications'
            os.system(f"start msedge {url}")

        case _:
             messagebox.showerror("Input Error", "Select a Valid Option")
    if flag == True:
        status.config(text= f" Opening {input}...")



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

time_label = Label(fr1, text=f"Hello {username()} ", font=("arial", 20))
time_label.pack(pady=10)

showtime = Label(fr1, font=("Helvetica", 15), fg="black")
showtime.pack(pady=10)

# Call timeshow to start updating the time
timeshow()



# Dropdown
fr2 = Frame(st)
fr2.pack(pady=10)
options = ['Import Tool','Missing Image Processing Excel File','My Local server folder','My local folder','FireFox','RemotePC','Zoom','D2']
select = ttk.Combobox(fr2, values=options, width=20,font=("Helvetica", 14))
select.pack()

submit = Button(fr2, text="Submit", font=("arial", 15), command=display)
submit.pack(pady=10)

status = Label(fr2, text="Choose a Option", font=("arial", 15)) 
status.pack(pady=10)



st.mainloop()