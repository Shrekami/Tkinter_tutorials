import json
from tkinter import ttk
from tkinter import *

def get_leaders():
    with open("donkey_nice.json", "r") as file:
        data = json.load(file)

    def sort_by_score(user):
        return -user['score']
    sorted_users = sorted(data, key=sort_by_score)
    return sorted_users

def update_db(player_name,score):
    with open("donkey_nice.json", "r") as file:
        found = False
        data = json.load(file)
        for user in data :
            if user['name'] == player_name:
                if score>user['score']:
                    user['score']=score
                found = True


        if found==False:
            data.append({"name":player_name,"score":score})

    with open("donkey_nice.json", "w+t",encoding='utf-8') as file:
        json.dump(data, file, indent=4,ensure_ascii=False)

def end(player_name, score):
    end_window = Toplevel()
    end_window['bg']='#2beade'
    bare = Label(end_window, text=f'{player_name} earned {score} points', bg="#dfa345")
    bare.place(x=200, y=5)
    end_window.geometry("800x600")

    leaderboard = Label(end_window, text="This is the leaderboard",bg='#4645df')
    leaderboard.place(x=200, y=45)

    update_db(player_name=player_name,score=score)

    leaders = get_leaders()
    number=1
    table=ttk.Treeview(end_window,show='headings',columns=('1','2','3'))
    table.heading("1", text="order")
    table.heading("2", text="name")
    table.heading("3", text="score")
    table.place(x=80,y=125)

    number=1
    for leader in leaders[:10]:
        table.insert("", END, values=(number, leader["name"], leader["score"]))
        number+=1