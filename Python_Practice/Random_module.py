import random
a= random.randint(1,3)  #---->both 1 and 3 included
b=int(input("enter a digit 1 or 2 or 3 : "))
if a==b:
    print("you won")
else:
    print("You lose")
c= random.randrange(1,3) #---> only 1 included 
print(c)
d= round(random.random()*100)
print(d)

l=[1,23,3443,45,55456,45]
a=random.choice(l)
print(a)

# text="My name is turjo"
# split_text=text.split(" ")
# print(split_text)
