import random
from tkinter import *
from ending import end

lives=2
points=0


def open_game_window(player_name):
    global rock, paper, scissors, computer_choice, winner
    game = Toplevel()

    def manp():
        name = entry.get()
        if len(name) <= 3:
            house["text"] = "Your username has to be longer than 3 characters"
            house['fg'] = "red"

        elif len(name) >= 3:
            print("Nice")

    romt = Button(text="Sign in", command=manp)
    romt.place(x=180, y=125)

    square = Label(text="Write your name")
    square.place(x=160, y=10)

    entry = Entry()
    entry.place(x=160, y=50)

    house = Label(text="")
    house.place(x=160, y=100)

    computer_choice=Label(game,text="computer_choice",width=100, height=6,bg="#52f5e8",font="12")
    computer_choice.pack()

    def get_computer_choice(my_choice):
        global computer_choice
        nlo=random.choice(["rock", "paper", "scissors"])
        computer_choice['text']=f"Computer chose {nlo}"
        print("Computer chose",nlo)
        win(my_choice=my_choice,machine_choice=nlo)

    winner=Label(game,text="Winner",width=40,bg="#5ff3d4",font="24")
    winner.pack(pady=70)

    def king(human):
        global winner
        name=player_name
        winner["text"]=f"{name} has {points} points and {lives}"
        if lives !=1:
            winner['text']+=" lives"
        else:
            winner['text']+=" life"

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
                # points += 100
                # print("You now have", points, "points")

            elif machine_choice=="scissors":
                human="computer"

                # if lives == 2:
                #     lives -= 1
                #     print("You now have", lives, "life")

                # elif lives == 1:
                #     lives -= 1
                #     print("You lost since you have", lives, "lives")
                #     rock.config(state="disabled")
                #     paper.config(state="disabled")
                #     scissors.config(state="disabled")
        if human == "human":
            points+=100
        elif human == "computer":
            lives-=1
            if lives ==0:
                rock.config(state="disabled")
                paper.config(state="disabled")
                scissors.config(state="disabled")
                game.withdraw()
                end(player_name=player_name,score=points)

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

    rock=Button(game,text="Rock",command=lambda:click_button(rock),width=5,height=1,bg="#f03521")
    rock.pack(pady=50,padx=10,fill="x",expand=True,side="left")

    paper=Button(game,text="Paper",command=lambda:click_button(paper),width=5,height=1,bg="#7af35f")
    paper.pack(padx=10,side="left",fill="x",expand=True)

    scissors=Button(game,text="Scissors",command=lambda:click_button(scissors),width=5,height=1,bg="#5f94f3")
    scissors.pack(padx=10,side="left",fill="x",expand=True)

# game.destroy()
# result=Tk()
# eah time you win earn 100 more points, you have two lives, make top player leader,add input for sign in