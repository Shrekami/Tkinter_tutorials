from tkinter import *
def noice(money):
    app = Tk()
    app.geometry("800x450+200+225")
    look = Label(app,text=f"You won {money} money", width=75, height=30, bg='blue')
    look.grid(row=1, column=3, padx=0, pady=0)
    app.mainloop()

def bad(lives):
    app = Tk()
    app.geometry("400x450+200+225")
    fiasco = Label(app, text=f"You lost because you had {lives} lives.", width=75, height=30, bg='blue')
    fiasco.grid(row=1, column=3, padx=0, pady=0)
    app.mainloop()
    # hmmmm