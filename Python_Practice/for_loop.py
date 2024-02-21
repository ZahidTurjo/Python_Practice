names=['a','b','c','d']
# for name in names:
#     print(name)

sets={3,4,65,7}
# for set in sets:
#     print(set)

# names="turjoi"
# for name in names:
#     print(name,"*")

# numbers=[2,3,4,5,-2]

# list=[]
# for number in numbers:
#     square=number**2
#     list.append(square)
#     print(list)

# print(list)

# numbers=[2,12,3,4,5,-2]

# for i in numbers:
    
#     if i%6==0:
#         print(i)
#         break
# else:
#     print("successfully completed")
# sum=1
# for i in range(1,100+1):
#     if i%2==0:
#         sum=sum+i
#         print(i)

# print("sum of even numbers =",sum)        

for i in range(1,101):
    if(i%5==0 and i%3==0):
        print(i,"FizzBUzz")    
    elif i%3 ==0:
        print(i,"Fizz")
    elif i%5==0:
        print(i,"Buzz")
    else:
        print(i)
  