import random
from tkinter import *
app=Tk()
app.geometry("600x500+400+50")
app.title("Robot")
app["bg"]="#527bf5"

computer_choice=Label(text="computer_choice",width=62, height=6,bg="#52f5e8")
computer_choice.pack()

def get_computer_choice(my_choice):
    global computer_choice
    nlo=random.choice(["rock", "paper", "scissors"])
    computer_choice['text']=f"Computer chose {nlo}"
    print("Computer chose",nlo)
    win(my_choice=my_choice,machine_choice=nlo)

winner=Label(text="Winner",width=40,bg="#5ff3d4")
winner.pack(pady=70)

def king(human):
    global winner
    winner["text"]=f"The winner is {human}"
    color(human)
def color(human):
    if human=="nobody":
        winner["bg"]="#f1a14c"
    elif human=="computer":
        winner["bg"]="#d164e4"
    elif human=="human":
        winner["bg"]="#189b4b"

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

def yay(chosen):
    rock.config(bd=5, relief="flat")
    paper.config(bd=5, relief="flat")
    scissors.config(bd=5, relief="flat")

    chosen.config(bd=5,relief="raised")

def click():
    print("You chose rock")
    yay(rock)
    get_computer_choice(my_choice="rock",)

def clank():
    print("You chose paper")
    yay(paper)
    get_computer_choice(my_choice="paper")

def clonk():
    print("You chose scissors")
    yay(scissors)
    get_computer_choice(my_choice="scissors")

rock=Button(text="Rock",command=click,width=6,height=1,bg="#f03521",)
rock.pack(pady=100,padx=10,fill="x",expand=True,side="left")

paper=Button(text="Paper",command=clank,width=6,height=1,bg="#7af35f")
paper.pack(padx=10,side="left",fill="x",expand=True)

scissors=Button(text="Scissors",command=clonk,width=6,height=1,bg="#5f94f3")
scissors.pack(padx=10,side="left",fill="x",expand=True)

app.mainloop()
# make a frame to each button that you press