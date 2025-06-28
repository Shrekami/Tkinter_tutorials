
print("Game\"Who wants to be a millionare\"")
pod50=True
podzn=True
summa=0
n_summa=0
def dost_podskazki():
    print("\t\t\t\t current sum:",summa)
    print("\t\t\t\t available hints:")
    if pod50 == True and podzn == True:
        print ("\t\t\t\t*****")
        print("\t\t\t\t* 50 over 50")
        print("\t\t\t\t*****")
        print("\t\t\t\t* Help from a player")
        print("\t\t\t\t*****")
    if pod50 == True and podzn == False:
        print("\t\t\t\t*****")
        print("\t\t\t\t*50 over 50*")
        print("\t\t\t\t*****")
    if pod50 == False and podzn ==True:
        print("\t\t\t\t*****")
        print("\t\t\t\t* Help from a player")
        print("\t\t\t\t*****")
    if pod50 ==False and podzn == False:
        print("\t\t\t\t*****")
        print("\t\t\t\t*There are no more hints*")
        print("\t\t\t\t*****")
def podskazki(a, b):
    global pod50
    global podzn
    question= input("Do you want a hint?")
    if question =="Yes" or question =="Yes" or question =="Yes":
        if pod50 ==False and podzn == False:
            print("There are no more hints")
    elif pod50 ==True and podzn == True:
        pods =input("50 over 50 or help from a player?")
    elif pod50 ==True and podzn == False:
        pods = input("50 over 50?")
    elif pod50 ==False and podzn ==True:
        pods =input("Help from a player?")
    if pods == "50 over 50":
        print("1.", a, "\t)2.", b)
        pod50 =False
    elif pods =="Help from a player":
        print("1.", b)
        podzn = False
    else:
        print("Incorrect choice!")
def question(a, b, a1, a2, a3, a4):
    print("Answer No" + str(a))
    print(b)
    print("1.", a1, "\t2.",a2)
    print("3.", a3, "\t4.", a4)
def loose(a):
    print("Sorry, but you lost!")
    print("Your prise has", n_summa, "Dollars")
Continue = True
Number = 0
begin = input("Do you want to start the game?")
if begin == "Yes" or begin =="yes" or begin == "YES":
    dost_podskazki()
    ques ="What continent has only 1 country?"
    question(1, question, "Europe", "Asia", "Africa", "Australia")
    podskazki("Europe", "Australia")
    answer =input("Type your answer:")
    if answer == "Australia":
        print("Nice! You got the right answer")
        summa = 500
else:
    Continue = False
if Continue == False:
    loose(n_summa)
else:
    dost_podskazki()
    ques ="How many letters are in the Ukranian alphabet?"
    question(2, ques, "28", "33", "31", "34")
    podskazki("33", "31")
    answer = input("Type an answer:")
    if answer == "33":
        print("Good job!You gave the right answer")
        summa = 1000
    else:
        Continue = False
if Continue == False:
    loose(n_summa)
else:
    dost_podskazki()
    ques = "How is a currency in India called?"
    question(3,ques, "Dollars", "Grivni", "Ruppe", "Pesos")
    podskazki("pesos", "ruppe")
    answer = input("Type an answer:")
if answer =="Ruppe":
    print("Wonderful!You have the right answer!")
    summa = 2000
else:
    Continue = False
if Continue == False:
    loose(n_summa)
else:
    dost_podskazki()
    ques = ("How is portrait called, when it is written by yourself?")
    question(4,ques,"Samoslaw","Self-recording", "Zerkalnik","Auto portrait")
    podskazki("Self-recording", "Auto portrait")
    answer = input("Type an answer:")
if answer =="Auto portrait":
    print("Astonishing!You gave the right answer!")
    summa = 5000
else:
    Continue = False
if Continue == False:
    loose (n_summa)
else:
    dost_podskazki()
    ques ="What is the name of the most expensive car type"
    question(5,ques, "Bugatti", "Lamborghini", "Audi","Mercedes")
    podskazki("Bugatti", "Lamborghini")
    answer = input("Type an answer:")
if answer == "Bugatti":
    print("Wow!You gave the right answer!")
    summa =10000
else:
    Continue =False
if Continue ==False:
    loose(n_summa)
else:
    dost_podskazki()
    ques= "In what game is the ball not involved"
    question(6,ques, "Basketball", "Tennis", "Baseball", "Kerling")
    podskazki("Tennis", "Kerling")
    answer = input("Type an answer:")
if answer == "Kerling":
    print("Unbelievable!You gave the right answer")
    summa=25000
else:
    Continue =False
if Continue ==False:
    loose(n_summa)
else:
    dost_podskazki()
    ques ="Which element is the most common on Earth?"
    question(7,ques, "Iron", "Nickel", "Silicon","Coal")
    podskazki("Iron", "Coal")
    answer = input("Type an answer:")
if answer =="Iron":
    print("7th in a row!You gave the right answer")
    summa =100000
else:
    Continue = False
if Continue ==False:
    loose(n_summa)
else:
    dost_podskazki()
    ques= "Who is a writer out of these people"
    question(8,ques,"Jean-Claude Van Damme", "Claude Monet", "Usain Bolt", "Edgar Po")
    podskazki("Claude Monet", "Edgar Po")
    answer =input("Type an answer:")
if answer =="Edgar Po":
    print ("Coming in hot!You gave the right answer")
    summa =250000
else:
    Continue = False
if Continue == False:
    loose(n_summa)
else:
    dost_podskazki()
    ques= "Who was/is the richest person on Earth?"
    question(9,ques, "Elon Musk","Jeffrey Bezos","Mansa Musa", "Cristiano Ronaldo")
    podskazki("Elon Musk", "Mansa Musa")
    answer = input("Type an answer:")
if answer == "mansa musa":
    print("Fabulous!You had given the right answer")
    summa = 500000
else:
    Continue = False
if Continue ==False:
    loose(n_summa)
else:
    dost_podskazki()
    ques ="What muscle does the brain mostly use for laughing"
    question(10,ques, "Orbicularis Oculi", "Temperal Lobe", "Motor Cortex", "Sensory Cortex")
    podskazki("Orbicularis Oculi", "Sensory Cortex")
    answer =input("Type the last answer:")
if answer == "Orbicularis Oculi":
    print("You rocketed through the questions!You also gave the right answer!")
    summa = 1000000
    print("You won the super prize!!!!!!Congratulations!!!!!!!!")
    print("Your win contains", summa,"Dollars")
else:
    Continue = False
    loose(n_summa)