import random
from tkinter import *
app=Tk()
app.geometry("600x500+400+50")
app.title("Robot")

computer_choice=Label(text="computer_choice",width=12, height=14)
computer_choice.pack()

winner=Label(text="Winner")
winner.pack()

def click():
    print("You chose rock")

def clank():
    print("You chose paper")

def clonk():
    print("You chose scissors")

rock=Button(text="Rock",command=click,width=6,height=1,fg="#000000",)
rock.pack(padx=10,fill="x",expand=True,side="left")

paper=Button(text="Paper",command=clank,width=6,height=1,fg="#000000")
paper.pack(padx=10,side="left",fill="x",expand=True)

scissors=Button(text="Scissors",command=clonk,width=6,height=1,fg="#000000")
scissors.pack(padx=10,side="left",fill="x",expand=True)

app.mainloop()
#if you press a button it needs to show you computer choice, for that use random.choice([rock,paper,scissor])
# !!!If the button is pressed, the function specified in the command is executed