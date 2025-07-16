from tkinter import *
import random
app=Tk()
app.geometry("500x500")
# a=5
# print(f'{"DONKEY" if a>0 else "SHREK"}')
#
def discriminant():
    global explain
    discriminants=b ** 2 - 4 * a * c
    global monkey
    global king_kong


    monkey['text']=("D=b^2-4ac=" #dont touch
                    f"{b**2}{f'+{a*c*-4}' if a*c*-4>0 else a*c*-4 }={discriminants}\n " # change this
                            "x1=(-b+sqrt(d))/2a\n" #dont touch sqrt is d**(1/2)
                            f"x1={(-b+discriminants**(1/2))/2*a} if {discriminants>0} else {(+b+discriminants**(1/2))/2*a} \n"# change this
                            "x2=(-b -sqrt(d))/2a\n" #dont touch
                            f"x2={(-b-discriminants**(1/2))/2*} if {discriminants>0} else you can't do that\n")# change this return calculating if discriminants>0 also 18 row also change the + - thingy
    monkey.pack()
    explain['text']=''
    king_kong['text']=''

explain=None
king_kong=None
monkey=None
a=1
b=-4
c=5
def discriminantiv2():
    global explain
    global monkey
    global king_kong
    monkey['text'] = (f"x1*x2=c\n"#dont touch
                      f"x1+x2=-b\n"#dont touch
                      f"x1*x2=c\n if {c>0} else you can't solve this"# change -5
                      f"x1+x2=b\n if {b>0} else you cant solve this"# change -4
                      f"x1=c x2=a\n") # change this
    explain['text']=''

def theory():
    global explain,monkey,king_kong
    app.destroy()
    app1=Tk()
    app1.geometry("500x500")
    group = StringVar(value =0)
    king_kong=Label(text='')

    a_text = f"{a}"
    b_text= f"{b}"
    if a == 1 or a == -1:
        a_text = a_text.replace("1","")
    if b==1 or b==-1:
        b_text = b_text.replace("1", "")

    squared=Label(text=f'{a_text}x^2+{b_ext}x{f"+{c}"if c>0 else c}')
    squared.pack()

    vieta_d=Radiobutton(command=discriminant,text="Discriminant",variable=group,value=1)
    vieta_d.pack()

    vieta_t=Radiobutton(command=discriminantiv2,text="viat",variable=group,value=2)
    vieta_t.pack()

    monkey=Label(text='')
    monkey.pack()
    explain=Label(text="These 2 choices are the variants of how you can calculate the square root.")
    explain.place(x=50,y=250)
    app.mainloop()

def sign():
    name=Entry()
    name.pack()

    number = Entry()
    number.pack()

    donkey = Entry()
    donkey.pack()

    equation=Button(command=theory,text="Lets start")
    equation.place(x=210,y=220)

sign()
app.mainloop()