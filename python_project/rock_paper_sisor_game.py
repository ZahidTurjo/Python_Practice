# rock wins again scissors, scissors win against papers, paper wins agaisnt rock

import random
r=0
p=1
s=2
your_choice=int(input("enter your choice = "))
computer_choice= random.randint(0,2)
print(computer_choice)

if(your_choice == r and computer_choice == s):
    print("You won")
elif your_choice == s and computer_choice == p:
    print("You won")
elif your_choice == p and computer_choice == r:
    print("You won")
elif your_choice == computer_choice:
    print("Draw the match")
else:
    print("Your friends will won the game")


