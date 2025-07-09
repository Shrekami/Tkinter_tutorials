from tkinter import *
app=Tk()
app.geometry("1000x500")
app.resizable(False,False)
bam=Canvas(width=1000,height=500,bg='green')
bam.pack()
ball_x=5
ball_y=5
num1=0
num2=0
bam.create_line(500,0,500,500,
                fill='white',
                dash=(1,20))
ball=bam.create_oval(500,250,525,275,
                fill='white')
plat1=bam.create_rectangle(10,200,20,300,width=5,
                fill='white')
plat2=bam.create_rectangle(970,200,980,300,width=5,
                fill='white')
text1=bam.create_text(250,20,text=num1,font='Arial 30')

text2=bam.create_text(750,20,text=num2,font='Arial 30')

bam.focus_set()

def moving(event):
    if bam.coords(plat1)[1]-20>0 and event.keysym=='w':
        bam.move(plat1,0,-20)
    if bam.coords(plat2)[1]-20>0 and event.keysym=='Up':
        bam.move(plat2,0,-20)
    if bam.coords(plat1)[3] + 20 < 600 and event.keysym == 's':
        bam.move(plat1, 0, 20)
    if bam.coords(plat2)[3] + 20 < 600 and event.keysym == 'Down':
        bam.move(plat2, 0, 20)


def roll():
    global ball_x,ball_y,num1,num2,text1,text2

    if bam.coords(ball)[3]>500 or bam.coords(ball)[3]==500:
        ball_y=-ball_y

    elif bam.coords(ball)[1] < 0 or bam.coords(ball)[1] == 0:
        ball_y = -ball_y

    elif bam.coords(ball)[0] <0 or bam.coords(ball)[0] == 0:
        ball_x = -ball_x

    if bam.coords(ball)[2] >= 1000:
        ball_x = -ball_x
        num1 += 1
        bam.delete(text1)
        text1 = bam.create_text(250, 20, text=num1, font='Arial 30')

    elif bam.coords(ball)[0] <=5:
        ball_x = -ball_x
        num2 += 1
        bam.delete(text2)
        text2 = bam.create_text(750, 20, text=num2, font='Arial 30')
    bam.move(ball, ball_x, ball_y)
    bam.after(15, roll)

    if bam.coords(ball)[2]>bam.coords(plat2)[0] and bam.coords(ball)[2]<bam.coords(plat2)[2] and bam.coords(ball)[3]>bam.coords(plat2)[1] and bam.coords(ball)[3]<bam.coords(plat2)[3]:
        ball_x=-ball_x
        ball_y=ball_y

    if bam.coords(ball)[0]>bam.coords(plat1)[0] and bam.coords(ball)[0]<bam.coords(plat1)[2] and bam.coords(ball)[1]>bam.coords(plat1)[1] and bam.coords(ball)[1]<bam.coords(plat1)[3]:
        ball_x=-ball_x
        ball_y=ball_y

roll()
bam.bind('<w>',moving)
bam.bind('<s>',moving)
bam.bind('<Up>',moving)
bam.bind('<Down>',moving)
app.mainloop()