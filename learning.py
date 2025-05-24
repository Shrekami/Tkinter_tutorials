import tkinter
from Fun_game import app as second_window
from tkinter import *
app1=Tk()
app1.geometry("500x250+100+75")



def manp():
    name=entry.get()
    if len(name)<=3:
        house["text"]="Your username has to be longer than 3 characters"
        house['fg']="red"

    elif len(name)>=3:
        app1.destroy()
        second_window.mainloop()

romt=Button(text="Sign in", command=manp)
romt.place(x=180,y=125)

square=Label(text="Write your name")
square.place(x=160,y=10)

entry=Entry()
entry.place(x=160,y=50)

house=Label(text="")
house.place(x=160,y=100)
app1.mainloop()