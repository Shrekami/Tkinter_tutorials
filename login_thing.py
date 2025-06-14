from tkinter import *
app=Tk()
app.geometry('800x800')

def new_game():
    pass

def exit():
    pass

game=Button(text='New game',command=new_game,width=115, height=25,bg='blue')
game.grid(row=1,column=1)

exiting=Button(text='Exit',command=exit,width=115, height=25,bg='yellow')
exiting.grid(row=6,column=1,pady=15)
app.mainloop()