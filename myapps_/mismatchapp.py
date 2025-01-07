import tkinter as tk
from tkinter import messagebox
import pandas as pd
from io import StringIO

def find_mismatches(data1, data2):
    df1 = pd.read_csv(StringIO(data1), header=None)
    df2 = pd.read_csv(StringIO(data2), header=None)
    mismatches = df1[~df1[0].isin(df2[0])].dropna()
    return sorted(list(set(mismatches[0].to_list()))) if not mismatches.empty else ["No mismatches found"]

def on_compare_button_click(event=None):
    data1 = text_area1.get("1.0", tk.END).strip()
    data2 = text_area2.get("1.0", tk.END).strip()
    if not data1 or not data2:
        messagebox.showerror("Error", "Please fill both data fields.")
        return
    mismatches = find_mismatches(data1, data2)
    output_text_area.delete("1.0", tk.END)
    output_text_area.insert(tk.END, "\n".join(mismatches))

window = tk.Tk()
window.title("Data Mismatch Finder")
window.geometry("400x500")

label1 = tk.Label(window, text="Enter the first set of data (one value per line):")
label1.pack(pady=5)
text_area1 = tk.Text(window, height=6, width=40)
text_area1.pack(pady=5)

label2 = tk.Label(window, text="Enter the second set of data (one value per line):")
label2.pack(pady=5)
text_area2 = tk.Text(window, height=6, width=40)
text_area2.pack(pady=5)

compare_button = tk.Button(window, text="Compare", command=on_compare_button_click)
compare_button.pack(pady=10)

label3 = tk.Label(window, text="Mismatched Values:")
label3.pack(pady=5)
output_text_area = tk.Text(window, height=6, width=40)
output_text_area.pack(pady=5)

window.bind('<Return>', on_compare_button_click)

window.mainloop()
