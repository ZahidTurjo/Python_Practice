#find out how many days, weeks,months we have left if we have until 90 years old
# age=int(input("enter the age ="))
# years_left=90-age
# month=years_left*12
# days=years_left*365
# weeks=years_left*52
# print("Years: ",years_left)
# print("Months :",month)
# print("Days :",days)
# print("weeks :", weeks)

#even or odd

# number=int(input("enter a number :"))
# if(number%2 == 0):
#     print("the number is even")
# else:
#     print("the number is odd")

#check whetther year is leap year is not

# year= int(input("enter the year :"))
# if year%4 == 0:
#     if year%100 == 0:
#         if year%400 == 0:
#             print("leap Year")
#         else:
#             print("This is not leap year")

#     else:
#         print("leap year")
    
# else:
#     print("This is not Leap Year")


  
 #select a random name from a list of names & the person selected who 
# will pay the everybodys foob bill

import random
name=input("enter the all name :")
split_name=name.split(",")
name_list=[]
name_list.extend(split_name)
print(name_list)
choice=random.choice(name_list)
print(f"{choice} will pay the everybody's bill") 

