import random
from tkinter import *
app=Tk()
app.geometry("600x500+400+50")
app.title("Robot")
app["bg"]="#527bf5"

lives=2
points=0

computer_choice=Label(text="computer_choice",width=100, height=6,bg="#52f5e8",font="12")
computer_choice.pack()

def get_computer_choice(my_choice):
    global computer_choice
    nlo=random.choice(["rock", "paper", "scissors"])
    computer_choice['text']=f"Computer chose {nlo}"
    print("Computer chose",nlo)
    win(my_choice=my_choice,machine_choice=nlo)

winner=Label(text="Winner",width=40,bg="#5ff3d4",font="24")
winner.pack(pady=70)

def king(human):
    global winner
    name=input("What is going to be your username? ")
    winner["text"]=f"{name} has {points} points and {lives} lives"
    color(human)

def color(human):
    if human=="nobody":
        winner["bg"]="#f1a14c"
    elif human=="computer":
        winner["bg"]="#d164e4"
    elif human=="human":
        winner["bg"]="#189b4b"

def win(my_choice,machine_choice):
    global lives
    global points
    if my_choice==machine_choice:
        human="nobody"
    if my_choice=="scissors":
        if machine_choice=="rock":
            human="computer"

            if lives==2:
                lives -= 1
                print("You now have", lives ,"life")

            elif lives==1:
                lives -= 1
                print("You lost since you have", lives ,"lives")
                rock.config(state="disabled")
                paper.config(state="disabled")
                scissors.config(state="disabled")

        elif machine_choice=="paper":
            human="human"
            points+=100
            print("You now have", points, "points")

    if my_choice=="rock":
        if machine_choice=="scissors":
           human="human"
           points+=200
           print("You now have", points, "points")

        elif machine_choice=="paper":
            human="computer"

            if lives == 2:
                lives -= 1
                print("You now have", lives, "life")

            elif lives == 1:
                lives -= 1
                print("You lost since you have", lives, "lives")
                rock.config(state="disabled")
                paper.config(state="disabled")
                scissors.config(state="disabled")

    if my_choice=="paper":
        if machine_choice=="rock":
            human="human"
            points += 300
            print("You now have", points, "points")

        elif machine_choice=="scissors":
            human="computer"

            if lives == 2:
                lives -= 1
                print("You now have", lives, "life")

            elif lives == 1:
                lives -= 1
                print("You lost since you have", lives, "lives")
                rock.config(state="disabled")
                paper.config(state="disabled")
                scissors.config(state="disabled")
    king(human)

def yay(chosen):
    rock.config(bd=5, relief="flat")
    paper.config(bd=5, relief="flat")
    scissors.config(bd=5, relief="flat")
    chosen.config(bd=5,relief="raised")

def click_button(chosen):
    print(f"You chose",chosen ["text"])
    yay(chosen)
    get_computer_choice(my_choice=chosen ["text"].lower())

rock=Button(text="Rock",command=lambda:click_button(rock),width=5,height=1,bg="#f03521")
rock.pack(pady=50,padx=10,fill="x",expand=True,side="left")

paper=Button(text="Paper",command=lambda:click_button(paper),width=5,height=1,bg="#7af35f")
paper.pack(padx=10,side="left",fill="x",expand=True)

scissors=Button(text="Scissors",command=lambda:click_button(scissors),width=5,height=1,bg="#5f94f3")
scissors.pack(padx=10,side="left",fill="x",expand=True)

# app.destroy()
# result=Tk()
app.mainloop()
# eact time you win earn 100 more points, you have two lives, make top player leader,add input for sign in