from tkinter import *
import json

from better_monopoly import friend_help

with open ('data_monopoly.json',"r") as file:
    data=json.load(file)
class characters:
    def __init__(self):
        self.app=Tk()
        self.app.geometry('800x800')
        with open('data_monopoly.json', "r") as file:
            self.data = json.load(file)
        self.number=-1
        self.first_window()
        
    def first_window(self):
        game = Button(text='New game',command=lambda: self.main_game(), width=115, height=25, bg='blue')
        game.grid(row=1, column=1)

        exiting = Button(text='Exit', command=exit, width=115, height=25, bg='yellow')
        exiting.grid(row=6, column=1, pady=15)
        self.app.mainloop()
        
    def main_game(self):
        self.app.destroy()
        self.count=16
        self.lives=1
        self.money=0
        self.game_window = Tk()
        self.game_window.geometry('800x800')
        self.create_interface()
        self.tick()
        self.update_question()
        self.game_window.mainloop()

    def update_question(self):
        self.count = 16
        self.number += 1
        self.gaming.config(state='normal')
        self.gaming1.config(state='normal')
        self.gaming2.config(state='normal')
        self.gaming3.config(state='normal')

        if self.number == 1:
            self.money += 1
            self.account_self['text'] = self.money

        if self.number == 2:
            self.money += 9
            self.account_self['text'] = self.money

        elif self.number == 3:
            self.money += 90
            self.account_self['text'] = self.money

        elif self.number == 4:
            self.money += 900
            self.account_self['text'] = self.money

        elif self.number == 5:
            self.money += 4000
            self.account_self['text'] = self.money


        elif self.number == 6:
            self.money += 15000
            self.account_self['text'] = self.money

        elif self.number == 7:
            self.money += 80000
            self.account_self['text'] = self.money

        elif self.number == 8:
            self.money += 200000
            self.account_self['text'] = self.money

        elif self.number == 9:
            self.money += 700000
            self.account_self['text'] = self.money

        if self.number == 10:
            self.game_window.destroy()
            self.neutral(status="win")

        else:
            self.showing["text"] = data[self.number]["question"]
            self.gaming["text"] = data[self.number]["choices"][0]
            self.gaming1["text"] = data[self.number]["choices"][1]
            self.gaming2["text"] = data[self.number]["choices"][2]
            self.gaming3["text"] = data[self.number]["choices"][3]

    def neutral(self, status):
        app = Tk()
        app['bg'] = 'yellow'
        app.geometry("800x450+200+225")
        if status == 'win':
            text = f"You won {self.money} money"

        elif status == "lose":
            text = "You lost because you had 0 lives."

        elif status == "good":
            text = f"Even though you lost, you earned {self.money} dollars."

        elif status == "nothing":
            text = "You lost because the time has run out."

        self.look = Label(app, text=text, width=75, height=30, bg='yellow')
        self.look.grid(row=1, column=4, padx=150, pady=0)

        app.mainloop()

    def tick(self):
        self.after_id = self.game_window.after(1000, self.tick)
        self.count -= 1
        self.timer["text"] = self.count
        if self.count == 0:
            self.game_window.destroy()
            self.neutral(status="nothing")

    def next_question(self,answer):
        if answer == data[self.number]["correct_answer"]:
            print("Nice you got the right answer")
            self.update_question()
        else:
            print("Wrong answer")
            self.lives -= 1
            self.account_self['text'] = self.money
            if self.lives == 0:
                self.game_window.after_cancel(self.after_id)
                self.game_window.withdraw()
                if self.number <= 5:
                    self.neutral(status="lose")

                if self.number >= 4:
                    self.neutral(status="good")

    def more_help(self):
        self.some_help.config(state='disabled')
        self.correct_answer = self.data[self.number]["correct_answer"]
        if self.correct_answer == 3:
            self.gaming.config(state='disabled')
            self.gaming2.config(state='disabled')

        elif self.correct_answer == 2:
            self.gaming1.config(state='disabled')
            self.gaming3.config(state='disabled')

        elif self.correct_answer == 1:
            self.gaming.config(state='disabled')
            self.gaming3.config(state='disabled')

        elif self.correct_answer == 0:
            self.gaming2.config(state='disabled')
            self.gaming3.config(state='disabled')

    def friend_help(self):
        self.friend.config(state='disabled')
        self.correct_answer = self.data[self.number]["correct_answer"]
        if self.correct_answer == 0:
            self.gaming1.config(state='disabled')
            self.gaming2.config(state='disabled')
            self.gaming3.config(state='disabled')

        elif self.correct_answer == 1:
            self.gaming.config(state='disabled')
            self.gaming2.config(state='disabled')
            self.gaming3.config(state='disabled')

        elif self.correct_answer == 2:
            self.gaming.config(state='disabled')
            self.gaming1.config(state='disabled')
            self.gaming3.config(state='disabled')

        elif self.correct_answer == 3:
            self.gaming.config(state='disabled')
            self.gaming1.config(state='disabled')
            self.gaming2.config(state='disabled')

    def money_total(self,money, money_take, game_window):
        self.app = Tk()
        self.app.geometry("500x500")
        self.app['bg'] = "aqua"
        self.total = Label(self.app, text=f'You took with yourself {money} dollars.', bg='blue')
        self.total.pack()
        self.game_window.destroy()
        self.app.mainloop()

    def create_interface(self):
        self.gaming = Button(text=self.data[self.number]["choices"][0], width=53, height=5, bg='blue')
        self.gaming.grid(row=9, column=0, padx=15, pady=8, columnspan=2)
        self.gaming.config(command=lambda: self.next_question(0))

        self.gaming1 = Button(text=data[self.number]["choices"][1], command=lambda: self.next_question(1), width=53, height=5,bg='blue')
        self.gaming1.grid(row=10, column=0, padx=15, pady=8, columnspan=2)

        self.gaming2 = Button(text=data[self.number]["choices"][2], command=lambda: self.next_question(2), width=53, height=5,bg='blue')
        self.gaming2.grid(row=9, column=2, padx=15, pady=8, columnspan=2)

        self.gaming3 = Button(text=data[self.number]["choices"][3], command=lambda: self.next_question(3), width=53, height=5,bg='blue')
        self.gaming3.grid(row=10, column=2, padx=2, pady=8, columnspan=2)

        self.some_help = Button(text="50/50", width=15, height=2, bg='green')
        self.some_help.grid(row=5, column=0, padx=20, pady=115)
        self.some_help.config(command=lambda: self.more_help())

        self.friend = Button(text="Help from a friend", width=15, height=2, bg='green')
        self.friend.grid(row=5, column=1, padx=20, pady=115, columnspan=2)
        self.friend.config(command=lambda: self.friend_help())

        self.money_take = Button(text="Get money", width=15, height=2, bg='green')
        self.money_take.grid(row=5, column=3, padx=20, pady=115)
        self.money_take.config(command=lambda: self.money_total(self.money, self.money_take, self.game_window))

        self.showing = Label(text=data[self.number]["question"], width=108, height=5, bg='aqua')
        self.showing.grid(row=6, column=0, padx=0, pady=12, columnspan=6)

        self.account_self = Label(text="0", width=18, height=3, bg='blue')
        self.account_self.grid(row=1, column=3, padx=0, pady=0)

        self.timer = Label()
        self.timer.grid(row=0, column=0)

game=characters()