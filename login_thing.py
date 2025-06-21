from tkinter import *

from better_monopoly import new_game

app=Tk()
app.geometry('800x800')


def exit():
    pass

game=Button(text='New game',command=lambda: new_game(app),width=115, height=25,bg='blue')
game.grid(row=1,column=1)

exiting=Button(text='Exit',command=exit,width=115, height=25,bg='yellow')
exiting.grid(row=6,column=1,pady=15)
app.mainloop()