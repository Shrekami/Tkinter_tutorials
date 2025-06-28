from tkinter import *
def neutral(money,status):
    app = Tk()
    app['bg'] = 'yellow'
    app.geometry("800x450+200+225")
    if status=='win':
        text=f"You won {money} money"

    elif status=="lose":
        text="You lost because you had 0 lives."

    elif status=="good":
        text = f"Even though you lost, you earned {money} dollars."

    elif status=="nothing":
        text = "You lost because the time has run out."

    look = Label(app, text=text, width=75, height=30, bg='yellow')
    look.grid(row=1, column=4, padx=150, pady=0)

    app.mainloop()