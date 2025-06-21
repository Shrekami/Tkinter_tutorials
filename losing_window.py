from tkinter import *
app=Tk()
app.geometry("400x450+200+225")

def bad():
    lost=Label(text="You lost",width=20,height=5)
    lost.grid(row=3,column=5)

app.mainloop()