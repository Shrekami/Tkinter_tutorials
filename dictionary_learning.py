# king=["Steven King",77,"writer","U.S.A",200]
# print(king[0])

# king={"name":"Steven King","age": 77,"job": "writer","country":"U.S.A","book_count": 200}
# king["age"]+=1
# print(king.get("age"))

# family={"brother":"Arsenii","mother":"Olha","dad":'Serhii'}
# for k1,v1 in family.items():
#     print(f"My {k1}s' name is {v1}")

# city="Seattle is a vibrant city in the Pacific Northwest, known for its iconic Space Needle, beautiful waterfront, and as the birthplace of tech giants like Microsoft and Amazon."
# myd={}
# for i in city.lower():
#     if i in myd.keys():
#         myd[i]+=1
#     else:
#         myd[i]=1
#         print(myd)
# myd=dict(sorted(myd.items()))
# for letter,count in myd.items():
#     print(letter,"appears", count,"times")
# myd['Seattle']=1111
# myd["seattle"]=2222
# print(myd)

# eat={"cucumber":3,"tomatoes":10,"banana":1,"watermelon":2}
#
# def add():
#     bor=input("What is the name of the new product, you would like to add? ")
#     fer=float(input("What will be the cost of your product? "))
#     eat[bor]=fer
#     print(eat)
#
# def refresh():
#     limb=input("Which product will you update cost? ")
#     romp=int(input("Type a new price "))
#     eat[limb]=romp
#     print(eat)
#
# def delete():
#   limp=input("Which product will you delete? ")
#   del eat[limp]
# #
# def pick():
#     for product,count in eat.items():
#         print(product,"with price of",count,"dollars")
#
# def count():
#     fomp = input("Which product will you get count of? ")
#     print(eat[fomp],'dollars')
#
# while True:
#     print("1 = Add new product")
#     print("2 = update_product_cost")
#     print("3 = Delete product")
#     print("4 = Get my products")
#     print("5 = Get product counts")
#     print("6 = Exit")
#     lomp=int(input("Choose your function "))
#     if lomp==1:
#         add()
#
#     elif lomp==2:
#         refresh()
#
#     elif lomp==3:
#         delete()
#
#     elif lomp==4:
#         pick()
#
#     elif lomp==5:
#         count()
#
#     elif lomp==6:
#         break


import json
with open("donkey_nice.json","r")as file:
    data=json.load(file)
    new_user={'name':"bob","age": 13,"score":100,"color":"hispanic"}
    data.append(new_user)
    print(data)
with open("donkey_nice.json","w+t")as file:
    json.dump(data,file,indent=4)