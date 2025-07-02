from tkinter import *
import json

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

        money_dict={0:0,1:1,2:9,3:90,4:900,5:4000,6:15000,7:80000,8:200000,9:700000}
        if self.number in money_dict.keys():
            self.money+=money_dict[self.number]
            self.account_self['text'] = self.money
            self.showing["text"] = data[self.number]["question"]
            self.gaming["text"] = data[self.number]["choices"][0]
            self.gaming1["text"] = data[self.number]["choices"][1]
            self.gaming2["text"] = data[self.number]["choices"][2]
            self.gaming3["text"] = data[self.number]["choices"][3]

        else:
            self.game_window.destroy()
            self.neutral(status="win")


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
        no_more_data={0:[self.gaming3,self.gaming2],1:[self.gaming2,self.gaming],2:[self.gaming1,self.gaming3],3:[self.gaming2,self.gaming]}
        self.correct_answer = self.data[self.number]["correct_answer"]
        button_for_disable=no_more_data[self.correct_answer]
        for button in button_for_disable:
            button.config(state='disabled')

    def friend_help(self):
        self.friend.config(state='disabled')
        data_for_disable = {0:self.gaming,1:self.gaming1,2:self.gaming2,3:self.gaming3}
        self.correct_answer = self.data[self.number]["correct_answer"]
        for choice,button in data_for_disable.items():
            if choice!=self.correct_answer:
                button.config(state="disabled")

    def money_total(self):
        self.app = Tk()
        self.app.geometry("500x500")
        self.app['bg'] = "aqua"
        self.total = Label(self.app, text=f'You took with yourself {self.money} dollars.', bg='blue')
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
        self.money_take.config(command=lambda: self.money_total())

        self.showing = Label(text=data[self.number]["question"], width=108, height=5, bg='aqua')
        self.showing.grid(row=6, column=0, padx=0, pady=12, columnspan=6)

        self.account_self = Label(text="0", width=18, height=3, bg='blue')
        self.account_self.grid(row=1, column=3, padx=0, pady=0)

        self.timer = Label()
        self.timer.grid(row=0, column=0)

game=characters()