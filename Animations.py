import random
from tkinter import *
from tkinter import font

score=0
def choose():
    global score
    score+=100000
    print(score)
    label["text"]=score
    if score>=1000000:
        button3.config(state="disabled")
        button1.config(state="disabled")
def background():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    app["bg"] = f'#{r:02x}{g:02x}{b:02x}'
def money():
    global score
    score+=1000000
    print(score)
    label["text"]=score
    if score>=1000000:
        button1.config(state="disabled")
        button3.config(state="disabled")

app=Tk()
app.geometry("500x500+400+100")
app["bg"]="#4165a4"
app.title("Fun")
app.resizable(False,True)

label_font = font.Font(slant="italic")
label=Label(text="This is a fun game where you get to choose buttons",bg="#5cc3e3",fg="#664eb4",font=label_font)
label.place(x=25,y=130)

button1=Button(text="This gives you 100,000 dollars now",command=choose)
button1.place(x=25,y=425)

button2=Button(text="Other background",command=background)
button2.place(x=200,y=50)

button3=Button(text="This gives 1 million dollars every 5 years",command=money)
button3.place(x=270,y=425)
app.mainloop()