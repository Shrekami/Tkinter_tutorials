# rendoo=[1,2,2]
# bleem=0
# for i in rendoo:
#     fleet=i**2
#     bleem+=fleet
# print(bleem)

# count=[1,2,3,4,5,6,7,8,9,10,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
# bam=0
# farm=0
# for i in count:
#     if i<0:
#         bam+=i
#     elif i>0:
#         farm+=1
# print(bam)
# print(farm)

# a=[1,2,2]
# b=[]
# for i in range(len(a)):
#     if a[i] not in b:
#         b.append(a[i])
# print(b)

# a=int(input('Type any range you want '))
# b=[]
# for i in range(1,a+1):
#     b.append(i)
# print(b)

# c=[1,3,2,5,4,8,6,9,7,18]
# d=[]
# for i in range(len(c)):
#     if i%2==0:
#         d.append(i)
# print(d)

# a=[1,2,3,3]
# b=[]
# c=0
# for i in a:
#     if i not in b:
#         b.append(i)
# for i in b:
#     print(i)
#     c+=i
# print(c)

# c=[11,12,13,14,15]
# d=0
# for i in range(len(c)):
#     if i%2!=0:
#         d+=c[i]**2
#     else:
#         d+=c[i]
# print(d)
#
# q=[1,2,"a","b"]
# w=[]
# for i in q:
#     if type(i)!=str:
#         w.append(i)
# print(w)

# a=[5,8,6,4]
# b=0
# c=0
# d=0
# if len(a) < 2:
#     print("-1")
# else:
#     for i in range(len(a)):
#         if a[i] > b:
#             b = a[i]
#     for i in range(len(a)):
#         c=b-a[i]
#         d+=c
#     print(d)

# a=[0,1,0]
# b=[]
# c=0
# for i in range(len(a)):
#     if a[i]>c:
#         c=a[i]
# for i in range(c+1):
#     b.append(i)
# print(b)

# a=[2,4,3,2,10]
# b=0
# c=0
# for i in range(len(a)):
#     if a[i]%2==0 and i<len(a)-1:
#         if a[i+1]%2==0:
#             b=a[i]
#             print('old i ',a[i])
#             c=a[i+1]
#             print('old i+1 ',a[i+1])
#             a[i+1]=b
#             print("NEW i+1",a[i+1])
#             a[i]=c
#             print("NEW i", a[i])

# e=[3,2,1,0]
# f=[]
# g="abcd"
# for i in g:
#     f.append(0)
# for i in range(len(g)):
#     f[e[i]]=g[i]
# print(f)

# a="eloquent"
# b=""
# c=""
# for i in range(len(a)):
#     if len(a)>2:
#         if i!=0:
#             if i!=len(a)-1:
#                 b=a[i]
#                 c+=b
# print(c)

# a="eloquent"
# print(a[1:-1])

# a=['apple','rottenBanana','apple']
# b=[]
# for i in range(len(a)):
#     if "rotten" in a[i]:
#         b=a[i].replace("rotten", "").lower()
#         a[i]=b
# print(a)

# a='recieve'
# b=''
# for i in range(len(a)):
    # if i<len(a)-1 and "e" in a[i] and "i" in a[i+1]:
    #     a=a.replace('ei',"ie")
    #     print(a)
#     ff = a.find('ei')
#     if ff!=-1:
#         a=a.replace("ei",'ie')
# print(a)

# a="abbcccdddda"
# b=[]
# for i in a:
#     if b and i ==b[-1]:
#         b.pop()
#     else:
#         b.append(i)
# print(b)
# use dictionary and +=1 and print odd number keys

# a="abbcccg"
# b={}
# c=[]
# for i in a:
#     if i in b:
#         b[i]+=1
#     else:
#         b[i]=1
# print(b)

# a='coDeWars'
# b=[]
# c=[True,b]
# for i in a:
#      if i.isupper():
#         b.append(i)
#         c[0]=False
# print(c)

# cart = {
#     "apple": 3,
#     "banana": 2,
#     "milk": 1
# }
# prices = {
#     "apple": 10,
#     "banana": 5,
#     "milk": 25
# }
# b=[]
# c=0
# for key,value in cart.items():
#     b=value*prices[key]
#     c+=b
# print(c)

# cart = {
#     "apple": 3,
#     "banana": 2,
#     "milk": 1,
#     'eggs':10
# }
# prices = {
#     "apple": 10,
#     "banana": 5,
#     "milk": 25,
#     'eggs':0.5
# }
# b=[]
# c={}
# for key,value in cart.items():
#     b=value*prices[key]
#     c[key]=b
# print(c)

# multiply cart by prices, and it has to equal the same amount as my_purchases,but print in dictionary form

# d=input("Type something ")
# engukr={
#     'water':'вода',
#     'fire':'вогонь',
#     'earth':'земля'
# }
# print(engukr.get(d,'No word'))

# c = {'Alex':
#     {
#     "type":"lion",
#     "hobby":"eating",
#     "best_friend":'Pumba'},
#     "Shrek":
#         {
#         "type":"ogre",
#         "hobby":"get swamp",
#         "best_friend":"Talking Donkey"}
# }
# b=[]
# for key,value in c.items():
#     print(f'{key},{value["hobby"]}')
