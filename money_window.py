from tkinter import *
def money_total(money):
    app=Tk()
    app.geometry("500x500")
    app['bg']="aqua"
    total=Label(app,text=f'You took with yourself {money} amount of money.')
    total.pack()
    app.mainloop()