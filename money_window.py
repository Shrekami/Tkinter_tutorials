from tkinter import *
def money_total(money,money_take):
    app=Tk()
    app.geometry("500x500")
    app['bg']="aqua"
    total=Label(app,text=f'You took with yourself {money} dollars.',bg='blue')
    total.pack()
    money_take.config(state='disabled')
    app.mainloop()