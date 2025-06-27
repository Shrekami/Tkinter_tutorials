from tkinter import *
def noice(money):
    app = Tk()
    app['bg']='yellow'
    app.geometry("800x450+200+225")
    look = Label(app,text=f"You won {money} money", width=75, height=30, bg='blue')
    look.grid(row=1, column=3, padx=0, pady=0)
    app.mainloop()

def bad():
    app = Tk()
    app['bg']='yellow'
    app.geometry("400x450+200+225")
    fiasco = Label(app, text="You lost because you had 0 lives.", width=75, height=30, bg='blue')
    fiasco.grid(row=1, column=3, padx=0, pady=0)
    app.mainloop()

def timely():
    app = Tk()
    app['bg'] = 'yellow'
    app.geometry("400x450+200+225")
    second = Label(app, text="You lost because the time has run out.", width=75, height=30, bg='blue')
    second.grid(row=1, column=3, padx=0, pady=0)
    app.mainloop()

    # hmmmm