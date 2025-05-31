import json
from tkinter import *

def get_leaders():
    with open("donkey_nice.json", "r") as file:
        data = json.load(file)

    def sort_by_score(user):
        return -user['score']
    #lambda user:-user["score"]
    sorted_users = sorted(data, key=sort_by_score)
    print(sorted_users)
    return sorted_users

def update_db(player_name,score):
    with open("donkey_nice.json", "r") as file:
        data = json.load(file)
        for user in data :
            if user['name'] == player_name:
                found = True
                break
            else:
                found=False

        if found ==False:
            data.append({"name":player_name,"score":score})
        else:
            print(player_name[score])
            print(user[score])
            if player_name[score]>=user[score]:
                data.append({"name": player_name, "score": score})
            else:
                pass

    # If user exist you need to compare actual score with score from json.
#If actual score i bigger than score from json , we should to update score from json,in another way dont do anything


    with open("donkey_nice.json", "w+t") as file:
        json.dump(data, file, indent=4)

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
    for leader in leaders[:5]:
        best=Label(end_window,text=f"{leader['name']} has {leader['score']} points",fg='#2bea7d')
        best.place(x=100,y=20+number*100)
        number+=1

# create Labels for leaderboard.In leaderboard show name of user and score

#update nice colors for login window and ending window