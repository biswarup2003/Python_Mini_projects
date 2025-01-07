import pyautogui
import time
import tkinter as tk
from tkinter import messagebox

# Correct credentials (you can change these values as needed)
CORRECT_ID = "admin"
CORRECT_PASSWORD = "@Biswarup2003"

# Function to run the automation script
def run_script():
    # Sheet change
    pyautogui.click(245, 991)

    # Formula section
    pyautogui.click(151, 285)
    pyautogui.click(735, 283, button='right')

    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.press('left')
    pyautogui.typewrite('ok', interval=0.05)
    
    # Write Ok
    pyautogui.moveTo(571, 264)
    pyautogui.doubleClick()

    # VLOOKUP section
    pyautogui.press('right')
    pyautogui.press('right')

    pyautogui.typewrite('=vlook', interval=0.05)
    pyautogui.press('enter')

    pyautogui.press('left')
    pyautogui.typewrite(',', interval=0.05)

    pyautogui.moveTo(289, 222, duration=0.1)
    pyautogui.dragTo(424, 227, duration=0.15)
    pyautogui.press('F4')
    pyautogui.press(',')
    pyautogui.press('2')
    pyautogui.press(',')
    pyautogui.press('0')
    pyautogui.press('enter')

    pyautogui.press('up')
    pyautogui.press('up')

    pyautogui.moveTo(859, 258)
    pyautogui.dragTo(1049, 251)

    pyautogui.hotkey('ctrl', 'shift', 'l')
    pyautogui.press('down')
    pyautogui.press('right')

    print("Automation started")

# Verify login credentials
def verify_login():
    entered_id = entry_id.get()
    entered_password = entry_password.get()

    if entered_id == CORRECT_ID and entered_password == CORRECT_PASSWORD:
        login_window.withdraw()  # Hide the login window
        open_automation_window()  # Open the automation window
    else:
        messagebox.showerror("Login Failed", "Contact to Biswarup Neogi")

# Open the main automation window
def open_automation_window():
    automation_window = tk.Tk()
    automation_window.geometry("200x100")
    automation_window.title("Formula")

    # Create a button to run the automation script
    button = tk.Button(automation_window, text="Run Automation", command=run_script, width=15, font=('arial', 15))
    button.pack(pady=40)

    # Bind the Enter key to run the automation script
    automation_window.bind("<Return>", lambda event: run_script())

    # Start the automation window loop
    automation_window.mainloop()

# Create the login window
login_window = tk.Tk()
login_window.geometry("400x300")
login_window.title("Login")

# ID field
label_id = tk.Label(login_window, text="ID:")
label_id.pack(pady=10)
entry_id = tk.Entry(login_window,show="*", width=30)
entry_id.pack(pady=10)

# Password field
label_password = tk.Label(login_window, text="Password:")
label_password.pack(pady=10)
entry_password = tk.Entry(login_window, show="*", width=30)
entry_password.pack(pady=10)

# Login button
button_login = tk.Button(login_window, text="Login", command=verify_login)
button_login.pack(pady=20)

# Start the login window loop
login_window.mainloop()
