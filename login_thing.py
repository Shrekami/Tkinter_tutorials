from tkinter import *
from better_monopoly import start_game
app = Tk()
app.geometry('800x800')
game = Button(app, text='New game', command=lambda :start_game(app), width=115, height=25, bg='blue')
game.grid(row=1, column=1)

exiting = Button(app, text='Exit', command=exit, width=115, height=25, bg='yellow')
exiting.grid(row=6, column=1, pady=15)

app.mainloop()

