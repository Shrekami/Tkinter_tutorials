from tkinter import *
from Fun_game import open_game_window
app=Tk()
app.geometry("500x250+100+75")
app['bg']="#332bea"


def manp():
    name=entry.get()
    if len(name)<=3:
        house["text"]="Your username has to be longer than 3 characters"
        house['fg']="red"

    elif len(name)>=3:
        app.withdraw()
        open_game_window(name)

romt=Button(app,text="Sign in", command=manp,bg="#2bd2ea")
romt.place(x=180,y=125)

square=Label(app,text="Write your name",bg="#ea5f2b")
square.place(x=160,y=10)

entry=Entry(app,bg="#d0ea2b")
entry.place(x=160,y=50)

house=Label(app,text="",bg='#65c441')
house.place(x=160,y=100,)
app.mainloop()
#