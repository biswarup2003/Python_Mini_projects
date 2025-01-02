from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import time
import getpass
import threading
import os

# Create the main window
st = Tk()
st.title("Welcome")
st.geometry("500x400")

# --------------------------------------------------------------------------------------------------------------
# Application for each department
deptm = {
    "HW": ['WPS Office', 'Microsoft Access', 'Zoom', 'Notepad', 'ICR(Latest)', 'Dynamic2', 'Learning Tool'],
    "MAP": ['WPS office', 'BravaReader'],
    "MEDICAL" : [],

}
# ----------------------------------------------------------------------------------------------------------------

# Functions
def update_options(event):
    dept = selectdept_combobox.get()
    option_combobox['values'] = deptm[dept]

def username():
    return getpass.getuser()

def timeshow():
    current_date = time.strftime("%d-%B-%Y")
    current_time = time.strftime("%H:%M:%S")
    text = f"{current_date}\n{current_time}"
    showtime.config(text=text)
    showtime.after(1000, timeshow)

def open_file(selected_option, path):
    try:
        if path.startswith('http'):
            # For URLs, open with a browser or default application
            os.startfile(path)
        else:
            os.startfile(path)  # Open executable file or application
        sts.config(text=f"Opening {selected_option}...")
    except Exception as e:
        messagebox.showerror("Error", f"Could not open {selected_option}")

def display():
    selected_option = option_combobox.get()
    paths = {
        'WPS Office': r"\\192.168.5.20\Software\Cmn_Apps_for_all\WPS_NEW.exe",
        'Microsoft Access': r"\\192.168.5.20\Software\HW_Software\AccessRuntime_X64.exe",
        'Zoom': r"",
        'ICR(Latest)': 'https://iimi1.capturedata.com:7553/review/',
        'Dynamic2': 'https://d-96671daae3.awsapps.com/start/#/?tab=applications',
        'Learning Tool': r"\\192.168.5.20\Software\HW_Software\IIMTraining.application"
    }

    if selected_option in paths:
        threading.Thread(target=open_file, args=(selected_option, paths[selected_option]), daemon=True).start()
    else:
        messagebox.showerror("Input Error", "Please select a valid option.")

# Main frame start
fr1 = Frame(st)
fr1.pack(pady=10)

time_label = Label(fr1, text=f"Hello {username()} ", font=("arial", 20))
time_label.pack(pady=10)

showtime = Label(fr1, font=("Helvetica", 15), fg="black")
showtime.pack(pady=10)
timeshow()


# Dropdown
fr2 = Frame(st)
fr2.pack(pady=10)

selectdept_combobox = ttk.Combobox(fr2,width=20,font=("Helvetica", 14) ,values=list(deptm.keys()))
selectdept_combobox.pack()
selectdept_combobox.bind("<<ComboboxSelected>>", update_options)


option_combobox = ttk.Combobox(fr2, width=20, font=("Helvetica", 14))
option_combobox.pack(pady=10)


#Submit
submit = Button(fr2, text="Submit", font=("arial", 15), command=display)
submit.pack(pady=10)

sts = Label(fr2, text="Choose an Option", font=("arial", 15)) 
sts.pack(pady=10)

st.mainloop()
