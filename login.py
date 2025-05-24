from tkinter import *
from Fun_game import open_game_window
app=Tk()
app.geometry("500x250+100+75")



def manp():
    name=entry.get()
    if len(name)<=3:
        house["text"]="Your username has to be longer than 3 characters"
        house['fg']="red"

    elif len(name)>=3:
        app.withdraw()
        open_game_window(name)

romt=Button(app,text="Sign in", command=manp)
romt.place(x=180,y=125)

square=Label(app,text="Write your name")
square.place(x=160,y=10)

entry=Entry(app)
entry.place(x=160,y=50)

house=Label(app,text="")
house.place(x=160,y=100)
app.mainloop()
