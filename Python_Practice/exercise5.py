#find the maximum number from a list of numbers

numbers=input("enter the numberrs : ")
list_numbers=numbers.split(" ")
count=0
for i in list_numbers:
    count=count+1
# print(count)  

for i in range(0,count):
    list_numbers[i]=int(list_numbers[i])
# print(list_numbers)
max=list_numbers[0]    
print("max", max)

for max_num in list_numbers:
    if max<max_num:
        max=max_num
print(max)        