from tkinter import *
app=Tk()
app.geometry('800x800')

def button1():
    pass

def button2():
    pass

def button3():
    pass

def button4():
    pass

def half_help():
    pass

def friend_help():
    pass

def audience_help():
    pass

gaming=Button(text="?",command=button1,width=53, height=5,bg='blue')
gaming.grid(row=9,column=1,padx=15,pady=8)

gaming1=Button(text="?",command=button2,width=53, height=5,bg='blue')
gaming1.grid(row=10,column=1,padx=15,pady=8)

gaming2=Button(text="?",command=button3,width=53, height=5,bg='blue')
gaming2.grid(row=9,column=2,padx=15,pady=8)

gaming3=Button(text="?",command=button4,width=53, height=5,bg='blue')
gaming3.grid(row=10,column=2,padx=2,pady=8)

some_help=Button(text="?",command=half_help,width=15, height=2,bg='green')
some_help.grid(row=5,column=2,padx=20,pady=135)

friend=Button(text="?",command=friend_help,width=15, height=2,bg='green')
friend.grid(row=5,column=4,padx=20,pady=135)

audience=Button(text="?",command=audience_help,width=15, height=2,bg='green')
audience.grid(row=5,column=6,padx=20,pady=135)

showing=Label(text="?",width=108, height=5,bg='aqua')
showing.grid(row=6,column=0,padx=0,pady=12,columnspan=6)

account_money=Label(text="?",width=18, height=3,bg='blue')
account_money.grid(row=1,column=6,padx=0,pady=0)

app.mainloop()