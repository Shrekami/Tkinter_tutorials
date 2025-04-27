from tkinter import *
from dont_open import Config
app=Tk()
app.geometry("500x625+400+50")
app["bg"]="#4eb4a1"
app.title("Calculator")
app.resizable(False,False)

zeronul=0
lblx=0
lbly=0
nul=0
def q(number):
    global nul, zeronul, lblx, lbly
    if nul == 0:
        nul = 1
        top["text"] = str(number)
    else:
        top["text"] += str(number)

    if zeronul == 0:
        lblx = int(top["text"])
    else:
        lbly = int(top["text"])

top=Label(text="This is a calculator that can count",width=50,height=10,bg="#4e92b4")
# top.place(x=80,y=50)
top.grid(row=0,column=0,columnspan=6,rowspan=2,pady=(5, 15))

def btrv():
    global znak,num,num2,lblx,lbly,nul,zeronul
    if znak =="+":
        top["text"]=str(lblx+lbly)
    elif znak =="-":
        top['text']=str(lblx-lbly)
    elif znak=="*":
        top['text']=str(lblx*lbly)
    elif znak =='/':
        if lbly==0:
            top["text"]="You can't divide by zero"
        else:
            top['text']=str(lblx/lbly)

    try:
        lblx=float(top['text'])
    except ValueError:
        lblx=0
    lbly=0
    nul=0
    zeronul=0
    num=0
    num2=0
    znak="n"

def btnznak(z):
    global nul,zeronul,znak
    top["text"]=top['text']+z
    nul=0
    zeronul=1
    znak=z

def clear():
    top['text']=''
    global zeronul,lblx,lbly,nul
    zeronul = 0
    lblx = 0
    lbly = 0
    nul = 0

button1=Button(text="1",command=lambda :q(1),width=5,height=2,bg=Config.button_bg,fg=Config.button_fg,font=Config.button_font)
button1.grid(row=2,column=0,padx=10,pady=10,ipadx=10)

button2=Button(text="2",command=lambda :q(2),width=5,height=2,bg=Config.button_bg,fg=Config.button_fg,font=Config.button_font)
button2.grid(row=2,column=1,padx=10,pady=10,ipadx=10)

button3=Button(text="3",command=lambda :q(3),width=5,height=2,bg=Config.button_bg,fg=Config.button_fg,font=Config.button_font)
button3.grid(row=2,column=2,padx=10,pady=10,ipadx=10)

button4=Button(text="4",command=lambda :q(4),width=5,height=2,bg=Config.button_bg,fg=Config.button_fg,font=Config.button_font)
button4.grid(row=2,column=3,padx=10,pady=10,ipadx=10)

button5=Button(text="5",command=lambda :q(5),width=5,height=2,bg=Config.button_bg,fg=Config.button_fg,font=Config.button_font)
button5.grid(row=3,column=0,padx=10,pady=10,ipadx=10)

button6=Button(text="6",command=lambda :q(6),width=5,height=2,bg=Config.button_bg,fg=Config.button_fg,font=Config.button_font)
button6.grid(row=3,column=1,padx=10,pady=10,ipadx=10)

button7=Button(text="7",command=lambda :q(7),width=5,height=2,bg=Config.button_bg,fg=Config.button_fg,font=Config.button_font)
button7.grid(row=3,column=2,padx=10,pady=10,ipadx=10)

button8=Button(text="8",command=lambda :q(8),width=5,height=2,bg=Config.button_bg,fg=Config.button_fg,font=Config.button_font)
button8.grid(row=3,column=3,padx=10,pady=10,ipadx=10)

button9=Button(text="9",command=lambda :q(9),width=5,height=2,bg=Config.button_bg,fg=Config.button_fg,font=Config.button_font)
button9.grid(row=4,column=0,padx=10,pady=10,ipadx=10)

button10=Button(text="0",command=lambda :q(0),width=5,height=2,bg=Config.button_bg,fg=Config.button_fg,font=Config.button_font)
button10.grid(row=4,column=1,padx=10,pady=10,ipadx=10)

button11=Button(text="+",command=lambda:btnznak("+"),width=5,height=2,bg=Config.button_bg,fg=Config.button_fg,font=Config.button_font)
button11.grid(row=4,column=2,padx=10,pady=10,ipadx=10)

button12=Button(text="-",command=lambda:btnznak("-"),width=5,height=2,bg=Config.button_bg,fg=Config.button_fg,font=Config.button_font)
button12.grid(row=4,column=3,padx=10,pady=10,ipadx=10)

button13=Button(text="*",command=lambda:btnznak("*"),width=5,height=2,bg=Config.button_bg,fg=Config.button_fg,font=Config.button_font)
button13.grid(row=5,column=0,padx=10,pady=10,ipadx=10)

button14=Button(text="/",command=lambda:btnznak("/"),width=5,height=2,bg=Config.button_bg,fg=Config.button_fg,font=Config.button_font)
button14.grid(row=5,column=1,padx=10,pady=10,ipadx=10)

button15=Button(text="=",command=btrv,width=5,height=2,bg=Config.button_equal_bg,fg=Config.button_fg,font=Config.button_font)
button15.grid(row=5,column=2,padx=10,pady=10,ipadx=10)

button16=Button(text="clear",command=clear,width=5,height=2,bg=Config.button_bg,fg=Config.button_fg,font=Config.button_font)
button16.grid(row=5,column=3,padx=10,pady=10,ipadx=10)
app.mainloop()

# Я зробив домашнє завдання, але синя штука не рухалася разом з цифрами. Як мені зробити так, щоб синя смужка стала посередині?