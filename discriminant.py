from tkinter import *
import random
app=Tk()
app.geometry("500x500")

def discriminant():
    app2 = Tk()
    app2.geometry("500x500")
    group = StringVar(value=0)
    monkey=Radiobutton(app2,text="D=b^2-4ac=16+20=36"
                            "x1=(-b+sqrt(d))/2a"
                            "x1=1.0"
                            "x2=(-b -sqrt(d))/2a"
                            "x2=-5.0")
    monkey.pack()

def discriminantiv2():
    app3 = Tk()
    app3.geometry("500x500")
    group = StringVar(value=0)
    king_kong=Radiobutton(app3,text="x1*x2=c x1+x2=-b x1*x2=-5 x1+x2=-4 x1=-5 x2=1")
    king_kong.pack()

def theory():
    app.destroy()
    app1 = Tk()
    app1.geometry("500x500")
    group = StringVar(value =0)

    squared=Label(text='1x^2+4x-5')
    squared.pack()

    vieta_d=Radiobutton(command=discriminant,text="Discriminant",variable=group,value=1)
    vieta_d.pack()

    vieta_t=Radiobutton(command=discriminantiv2,text="viat",variable=group,value=2)
    vieta_t.pack()

    explains=Label(text="These 2 choices are the variants of how you can calculate the square root.")
    explains.place(x=50,y=250)
    app1.mainloop()

def sign():
    name=Entry()
    name.pack()

    number = Entry()
    number.pack()

    donkey = Entry()
    donkey.pack()

    equation=Button(command=theory,text="Lets start")
    equation.place(x=150,y=150)

sign()
app.mainloop()