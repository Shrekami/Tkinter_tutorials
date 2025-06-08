from tkinter import *
from tkinter import messagebox
app=Tk()
app.geometry('800x800')
app['bg']='#332bea'

win=[0,0,0,0,0,0,0,0,0]
bee=100
boo=80
bii=20
buu=20
color='aqua'
xo=1

def rgb(button,index):
    global xo
    if win[index]==0:
        if xo==1:
            button['bg']='green'
            button.config(state='disabled')
            xo=2
            donkey=1
        else:
            button['bg']='red'
            button.config(state='disabled')
            xo=1
            donkey=2
        win[index]=donkey
        print(win)
    winning_positions()

def winning_positions():
    winner=0
    if win[0]==win[1]==win[2]!=0:
        winner=win[0]
        

    elif win[3]==win[4]==win[5]!=0:
        winner = win[3]
        
        
    elif win[6]==win[7]==win[8]!=0:
        winner = win[6]
        
        
    elif win[0]==win[3]==win[6]!=0:
        winner=win[0]
        
        
    elif win[1]==win[4]==win[7]!=0:
        winner=win[1]
        
        
    elif win[2]==win[5]==win[8]!=0:
        winner=win[2]
        
        
    elif win[1]==win[4]==win[7]!=0:
        winner = win[1]
        
        
    elif win[2]==win[4]==win[6]!=0:
        winner=win[2]
        
        
    elif win[0]==win[4]==win[8]!=0:
        winner = win[0]

    elif 0 not in win:
        messagebox.showinfo('winner','Draw')
        replay()
    if winner:
        if winner==1:
            messagebox.showinfo('winner', 'Green won')
        else:
            messagebox.showinfo('winner','Red won')
        replay()

def replay():
    global xo, win
    for i in buttons:
        i['bg']="aqua"
        i.config(state='normal')
    win=[0,0,0,0,0,0,0,0,0]
    xo=1

def escape(event):
    app.destroy()

def help(event):
    messagebox.showinfo('Tic tac toe','In this game you play a game of tic tac toe against each other you win by having to connect three green squares or red squares in any possible ways. Good luck')
    
buttons=[]
column=0
row=0
for i in range(9):
    button0=Button(bg=color)
    button0.grid(row=row,column=column,ipadx=bee,ipady=boo,padx=bii,pady=buu)
    button0.config(command=lambda b=i,button=button0:rgb(button,b))
    column+=1
    if column%3==0:
        column=0
        row+=1
    buttons.append(button0)

app.bind('<Escape>', escape)
app.bind('<h>',help)
app.bind('<q>',lambda e:rgb(buttons[0],0))
app.bind('<w>',lambda e:rgb(buttons[1],1))
app.bind('<e>',lambda e:rgb(buttons[2],2))
app.bind('<r>',lambda e:rgb(buttons[3],3))
app.bind('<t>',lambda e:rgb(buttons[4],4))
app.bind('<y>',lambda e:rgb(buttons[5],5))
app.bind('<u>',lambda e:rgb(buttons[6],6))
app.bind('<i>',lambda e:rgb(buttons[7],7))
app.bind('<o>',lambda e:rgb(buttons[8],8))
app.mainloop()
