from tkinter import *
from better_monopoly import money
app=Tk()
app.geometry("400x450+200+225")

def noicee():
    look=Label(text=f"You won {money} money",width=20,height=5)
    look.grid(row=3,column=5)

app.mainloop()