from tkinter import *
from winning_window import bad
from winning_window import noice
from winning_window import timely
from money_window import money_total
import json

count=15
game_window = None
lives = 1
money= 0
number = 0
gaming = None
gaming1 = None
gaming2 = None
gaming3 = None
showing = None
account_money = None
lives_label = None
timer=None

with open ('data_monopoly.json',"r") as file:
    data=json.load(file)

print(data[number])

def update_question():
    global number, money, account_money, showing, gaming, gaming1, gaming2, gaming3,count
    global money
    count=15
    number+=1
    gaming.config(state='normal')
    gaming1.config(state='normal')
    gaming2.config(state='normal')
    gaming3.config(state='normal')

    if number==1:
        money+=1
        account_money['text']=money

    if number==2:
        money+=9
        account_money['text'] = money

    elif number==3:
        money+=90
        account_money['text'] = money

    elif number==4:
        money+=900
        account_money['text'] = money

    elif number==5:
        money+=4000
        account_money['text'] = money
        account_money.config(state='disabled')

    elif number==6:
        money+=15000
        account_money['text'] = money

    elif number==7:
        money+=80000
        account_money['text'] = money

    elif number==8:
        money+=200000
        account_money['text'] = money

    elif number==9:
        money+=700000
        account_money['text'] = money

    if number==10:
        game_window.destroy()
        noice(money)

    else:
        showing["text"]=data[number]["question"]
        gaming["text"]=data[number]["choices"][0]
        gaming1["text"] = data[number]["choices"][1]
        gaming2["text"] = data[number]["choices"][2]
        gaming3["text"] = data[number]["choices"][3]

def next_question(answer):
    global gaming,gaming1,gaming2,gaming3,game_window
    global lives
    global money
    if answer==data[number]["correct_answer"]:
        print("Nice! You got the right answer")
        tick()
        update_question()
    else:
        print("Wrong answer")
        lives-=1
        money-=100
        account_money['text'] = money
        if lives==0:
            game_window.withdraw()
            bad()

def tick():
    global count, after_id,new_window,i,timer
    after_id = game_window.after(1000, tick)
    count-=1
    timer["text"]=count
    if count==0:
        game_window.withdraw()
        timely()


        # if count < 5:
        #     text = "Сума: 0"
        # else:
        #     text = "sum 1500"

def half_help(some_help):
    some_help.config(state='disabled')
    correct_answer=data[number]["correct_answer"]
    if correct_answer==3:
        gaming.config(state='disabled')
        gaming2.config(state='disabled')

    elif correct_answer==2:
        gaming1.config(state='disabled')
        gaming3.config(state='disabled')

    elif correct_answer==1:
        gaming.config(state='disabled')
        gaming3.config(state='disabled')

    elif correct_answer==0:
        gaming2.config(state='disabled')
        gaming3.config(state='disabled')

def friend_help(friend):
    friend.config(state='disabled')
    correct_answer=data[number]["correct_answer"]
    if correct_answer==0:
        gaming1.config(state='disabled')
        gaming2.config(state='disabled')
        gaming3.config(state='disabled')

    elif correct_answer==1:
        gaming.config(state='disabled')
        gaming2.config(state='disabled')
        gaming3.config(state='disabled')

    elif correct_answer==2:
        gaming.config(state='disabled')
        gaming1.config(state='disabled')
        gaming3.config(state='disabled')

    elif correct_answer==3:
        gaming.config(state='disabled')
        gaming1.config(state='disabled')
        gaming2.config(state='disabled')

# you take the money you have and create winning and losing window colors and features.

def create_interface():
    global lives, money, number
    global gaming, gaming1, gaming2, gaming3, showing, account_money, lives_label,timer
    gaming=Button(text=data[number]["choices"][0],width=53, height=5,bg='blue')
    gaming.grid(row=9,column=0,padx=15,pady=8,columnspan=2)
    gaming.config(command=lambda:next_question(0))

    gaming1=Button(text=data[number]["choices"][1],command=lambda:next_question(1),width=53, height=5,bg='blue')
    gaming1.grid(row=10,column=0,padx=15,pady=8,columnspan=2)

    gaming2=Button(text=data[number]["choices"][2],command=lambda:next_question(2),width=53, height=5,bg='blue')
    gaming2.grid(row=9,column=2,padx=15,pady=8,columnspan=2)

    gaming3=Button(text=data[number]["choices"][3],command=lambda:next_question(3),width=53, height=5,bg='blue')
    gaming3.grid(row=10,column=2,padx=2,pady=8,columnspan=2)

    some_help=Button(text="50/50",width=15, height=2,bg='green')
    some_help.grid(row=5,column=0,padx=20,pady=115)
    some_help.config(command=lambda: half_help(some_help))

    friend=Button(text="Help from a friend",width=15, height=2,bg='green')
    friend.grid(row=5,column=1,padx=20,pady=115,columnspan=2)
    friend.config(command=lambda:friend_help(friend))

    money_take=Button(text="Get money",width=15, height=2,bg='green')
    money_take.grid(row=5,column=3,padx=20,pady=115)
    money_take.config(command=lambda:money_total(money,money_take))

    showing=Label(text=data[number]["question"],width=108, height=5,bg='aqua')
    showing.grid(row=6,column=0,padx=0,pady=12,columnspan=6)

    account_money=Label(text="0",width=18, height=3,bg='blue')
    account_money.grid(row=1,column=3,padx=0,pady=0)

    timer=Label()
    timer.grid(row=0,column=0)

def new_game(app):
    global  game_window,timer
    app.destroy()
    game_window = Tk()
    game_window.geometry('800x800')
    create_interface()
    tick()
    game_window.mainloop()