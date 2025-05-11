import random
from tkinter import *
app=Tk()
app.geometry("600x500+400+50")
app.title("Robot")

computer_choice=Label(text="computer_choice",width=32, height=14)
computer_choice.pack()
def get_computer_choice(my_choice):
    global computer_choice
    nlo=random.choice(["rock", "paper", "scissors"])
    computer_choice['text']=f"Computer chose {nlo}"
    print("Computer chose",nlo)
    win(my_choice=my_choice,machine_choice=nlo)

winner=Label(text="Winner")
winner.pack()

def king(human):
    global winner
    winner["text"]=f"The winner is {human}"

def win(my_choice,machine_choice):
    if my_choice==machine_choice:
        human="nobody"
    if my_choice=="scissors":
        if machine_choice=="rock":
            human="computer"
        elif machine_choice=="paper":
            human="human"

    if my_choice=="rock":
        if machine_choice=="scissors":
           human="human"
        elif machine_choice=="paper":
            human="computer"

    if my_choice=="paper":
        if machine_choice=="rock":
            human="human"
        elif machine_choice=="scissors":
            human="computer"
    king(human)

def click():
    print("You chose rock")
    get_computer_choice(my_choice="rock")

def clank():
    print("You chose paper")
    get_computer_choice(my_choice="paper")

def clonk():
    print("You chose scissors")
    get_computer_choice(my_choice="scissors")

rock=Button(text="Rock",command=click,width=6,height=1,fg="#000000",)
rock.pack(padx=10,fill="x",expand=True,side="left")

paper=Button(text="Paper",command=clank,width=6,height=1,fg="#000000")
paper.pack(padx=10,side="left",fill="x",expand=True)

scissors=Button(text="Scissors",command=clonk,width=6,height=1,fg="#000000")
scissors.pack(padx=10,side="left",fill="x",expand=True)

app.mainloop()
#if you press a button it needs to show you computer choice, for that use random.choice([rock,paper,scissor])
# !!If the button is pressed, the function specified in the command is executed