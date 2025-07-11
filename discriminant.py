from tkinter import *
import random
app=Tk()
app.geometry("500x500")
group = StringVar(value =0)

def theory():
    app.destroy()
    app1 = Tk()
    app1.geometry("500x500")


    squared=Label(text='1x^2+4x-5')
    squared.pack()

    vieta_d=Radiobutton(text="Discriminant",variable=group,value=1)
    vieta_d.pack()

    vieta_t=Radiobutton(text="viat",variable=group,value=2)
    vieta_t.pack()
    app1.mainloop()

def sign():
    name=Entry()
    name.pack()

    number = Entry()
    number.pack()

    donkey = Entry()
    donkey.pack()

    equation=Button(command=theory,text="Lets start")
    equation.pack()

sign()
app.mainloop()