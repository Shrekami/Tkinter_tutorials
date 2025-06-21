from tkinter import *
import json

game_window = None
lives = 2
money = 0
number = 0
gaming = None
gaming1 = None
gaming2 = None
gaming3 = None
showing = None
account_money = None
lives_label = None

with open ('data_monopoly.json',"r") as file:
    data=json.load(file)

print(data[number])

def update_question():
    global number, money, account_money, showing, gaming, gaming1, gaming2, gaming3

    global money
    number+=1
    if number==2:
        money+=0
        account_money['text'] = money

    elif number==3:
        money+=10
        account_money['text'] = money

    elif number==4:
        money+=90
        account_money['text'] = money

    elif number==5:
        money+=900
        account_money['text'] = money

    elif number==6:
        money+=4000
        account_money['text'] = money

    elif number==7:
        money+=15000
        account_money['text'] = money

    elif number==8:
        money+=80000
        account_money['text'] = money

    elif number==9:
        money+=200000
        account_money['text'] = money

    if number==10:
        money+=700000
        account_money['text'] = money
        game_window.destroy()

    else:
        showing["text"]=data[number]["question"]
        gaming["text"]=data[number]["choices"][0]
        gaming1["text"] = data[number]["choices"][1]
        gaming2["text"] = data[number]["choices"][2]
        gaming3["text"] = data[number]["choices"][3]

def next_question(answer):
    global gaming,gaming1,gaming2,gaming3
    global lives
    global money
    if answer==data[number]["correct_answer"]:
        print("Nice! You got the right answer")
        update_question()
    else:
        print("Wrong answer")
        lives-=1
        money-=100
        account_money['text'] = money
        if lives==0:
            game_window.withdraw()

def half_help():
    pass

def friend_help():
    pass

def audience_help():
    pass
def create_interface():
    global lives, money, number
    global gaming, gaming1, gaming2, gaming3, showing, account_money, lives_label
    gaming=Button(text=data[number]["choices"][0],command=lambda:next_question(0),width=53, height=5,bg='blue')
    gaming.grid(row=9,column=0,padx=15,pady=8,columnspan=2)

    gaming1=Button(text=data[number]["choices"][1],command=lambda:next_question(1),width=53, height=5,bg='blue')
    gaming1.grid(row=10,column=0,padx=15,pady=8,columnspan=2)

    gaming2=Button(text=data[number]["choices"][2],command=lambda:next_question(2),width=53, height=5,bg='blue')
    gaming2.grid(row=9,column=2,padx=15,pady=8,columnspan=2)

    gaming3=Button(text=data[number]["choices"][3],command=lambda:next_question(3),width=53, height=5,bg='blue')
    gaming3.grid(row=10,column=2,padx=2,pady=8,columnspan=2)

    some_help=Button(text="?",command=half_help,width=15, height=2,bg='green')
    some_help.grid(row=5,column=0,padx=20,pady=115)

    friend=Button(text="?",command=friend_help,width=15, height=2,bg='green')
    friend.grid(row=5,column=1,padx=20,pady=115,columnspan=2)

    audience=Button(text="?",command=audience_help,width=15, height=2,bg='green')
    audience.grid(row=5,column=3,padx=20,pady=115)

    showing=Label(text=data[number]["question"],width=108, height=5,bg='aqua')
    showing.grid(row=6,column=0,padx=0,pady=12,columnspan=6)

    account_money=Label(text="?",width=18, height=3,bg='blue')
    account_money.grid(row=1,column=3,padx=0,pady=0)
# You have to check other way how to check for the win:Good
# Add money in the top label:Worked but doesn't work now because of the switching windows
# Winning and losing window: Confused
def new_game(app):
    app.destroy()
    game_window = Tk()
    game_window.geometry('800x800')
    create_interface()
    game_window.mainloop()