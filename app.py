from tkinter import *
st= Tk()
st.title('My app')
st.geometry('400x600')
# st.config(bg='pink')

def on_click():
    pass
def on_submit():
    input = ent1.get()
    label1.config(text=f'Your input : {input}')

label1 = Label(st,text='Welcome', font=("arial",15))
label1.pack(pady=20)

btn1 = Button(st, text="Click Me", font=("arial",15), command= on_click)
btn1.pack(pady=10)

ent1 = Entry(st,font=('arial',15))
ent1.pack(pady=10)

submit1 = Button(st, text="Submit",font=('arial',15), command=on_submit)
submit1.pack(pady=15)

frame1 = Frame(st)
frame1.pack(pady=10)

btn2 = Button(st, text='sum', command= lambda: print(ent1.get()) )
btn2.pack()

st.mainloop()

