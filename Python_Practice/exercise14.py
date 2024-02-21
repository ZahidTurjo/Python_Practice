#calclate the avarage height from a list of height
heights=input("enter the heightes and seperated each height by',': " )
list_of_height=heights.split(',')
sum=0
for height in list_of_height:

    sum=sum+int(height)

average_of_heigth=sum/len(list_of_height)
print(average_of_heigth)


