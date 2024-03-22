number= (input('enter a number: '))

list_num=list(number)
print(list_num)
for i in range(len(number)):
    list_num[i]=(int(list_num[i]))**(len(number))
print(list_num)

sum=0
for i in list_num:
    sum=sum+i

print(sum)

if sum == int(number):
    print(f"{number} is armstrong number")
else:
    print(f"the number is not armstrong")