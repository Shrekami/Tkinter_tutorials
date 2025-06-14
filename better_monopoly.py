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


gaming=Button(text="?",command=button1,width=53, height=5,bg='blue')
gaming.grid(row=12,column=1,padx=15,pady=2)

gaming1=Button(text="?",command=button2,width=53, height=5,bg='blue')
gaming1.grid(row=13,column=1,padx=15,pady=2)

gaming2=Button(text="?",command=button3,width=53, height=5,bg='blue')
gaming2.grid(row=12,column=2,padx=15,pady=2)

gaming3=Button(text="?",command=button4,width=53, height=5,bg='blue')
gaming3.grid(row=13,column=2,padx=2,pady=2)

showing=Label(text="?",width=106, height=5,bg='blue')
showing.grid(row=13,column=2,padx=2,pady=2)

app.mainloop()