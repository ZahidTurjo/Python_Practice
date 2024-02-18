love_name = input("enter your name : ").lower()
love_name2=input("enter his/her name : ").lower()
name=(love_name+love_name2)

t_count= name.count("t")
r_count= name.count("r")
u_count= name.count("u")
e_count= name.count("e")

sum1=t_count+r_count+u_count+e_count
print(sum1)

l_count= name.count("l")
o_count= name.count("o")
v_count= name.count("v")
e_count= name.count("e")

sum=l_count+o_count+v_count+e_count
print(sum)
love_percentage=str(sum1)+str(sum)

print (f"love percentage is {love_percentage}%")

if(int(love_percentage)<10 and int(love_percentage)>90):
    print("Like a blast")
elif int(love_percentage)>40:
    print("live together")
else:
    print("heart broken")
