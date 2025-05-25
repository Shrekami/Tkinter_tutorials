import random
from tkinter import *

class GameWindow:
    def __init__(self, player_name):
        self.player_name = player_name
        self.lives = 2
        self.points = 0

        self.game = Toplevel()

        self.computer_choice = Label(self.game, text="computer_choice", width=100, height=6, bg="#52f5e8", font="12")
        self.computer_choice.pack()

        self.winner = Label(self.game, text="Winner", width=40, bg="#5ff3d4", font="24")
        self.winner.pack(pady=70)

        self.rock = Button(self.game, text="Rock", command=lambda: self.click_button(self.rock), width=5, height=1, bg="#f03521")
        self.rock.pack(pady=50, padx=10, fill="x", expand=True, side="left")

        self.paper = Button(self.game, text="Paper", command=lambda: self.click_button(self.paper), width=5, height=1, bg="#7af35f")
        self.paper.pack(padx=10, side="left", fill="x", expand=True)

        self.scissors = Button(self.game, text="Scissors", command=lambda: self.click_button(self.scissors), width=5, height=1, bg="#5f94f3")
        self.scissors.pack(padx=10, side="left", fill="x", expand=True)

    def get_computer_choice(self, my_choice):
        nlo = random.choice(["rock", "paper", "scissors"])
        self.computer_choice['text'] = f"Computer chose {nlo}"
        print("Computer chose", nlo)
        self.win(my_choice=my_choice, machine_choice=nlo)

    def king(self, human):
        name = 'donkey'
        self.winner["text"] = f"{name} has {self.points} points and {self.lives} lives"
        self.color(human)

    def color(self, human):
        if human == "nobody":
            self.winner["bg"] = "#f1a14c"
        elif human == "computer":
            self.winner["bg"] = "#d164e4"
        elif human == "human":
            self.winner["bg"] = "#189b4b"

    def win(self, my_choice, machine_choice):
        if my_choice == machine_choice:
            human = "nobody"
        elif my_choice == "scissors":
            if machine_choice == "rock":
                human = "computer"
                if self.lives == 2:
                    self.lives -= 1
                    print("You now have", self.lives, "life")
                elif self.lives == 1:
                    self.lives -= 1
                    print("You lost since you have", self.lives, "lives")
                    self.disable_buttons()
            elif machine_choice == "paper":
                human = "human"
                self.points += 100
                print("You now have", self.points, "points")
        elif my_choice == "rock":
            if machine_choice == "scissors":
                human = "human"
                self.points += 200
                print("You now have", self.points, "points")
            elif machine_choice == "paper":
                human = "computer"
                if self.lives == 2:
                    self.lives -= 1
                    print("You now have", self.lives, "life")
                elif self.lives == 1:
                    self.lives -= 1
                    print("You lost since you have", self.lives, "lives")
                    self.disable_buttons()
        elif my_choice == "paper":
            if machine_choice == "rock":
                human = "human"
                self.points += 300
                print("You now have", self.points, "points")
            elif machine_choice == "scissors":
                human = "computer"
                if self.lives == 2:
                    self.lives -= 1
                    print("You now have", self.lives, "life")
                elif self.lives == 1:
                    self.lives -= 1
                    print("You lost since you have", self.lives, "lives")
                    self.disable_buttons()
        self.king(human)

    def disable_buttons(self):
        self.rock.config(state="disabled")
        self.paper.config(state="disabled")
        self.scissors.config(state="disabled")

    def yay(self, chosen):
        self.rock.config(bd=5, relief="flat")
        self.paper.config(bd=5, relief="flat")
        self.scissors.config(bd=5, relief="flat")
        chosen.config(bd=5, relief="raised")

    def click_button(self, chosen):
        print(f"You chose", chosen["text"])
        self.yay(chosen)
        self.get_computer_choice(my_choice=chosen["text"].lower())

