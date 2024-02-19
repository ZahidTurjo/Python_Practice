# tuple1=(10,) #--->comma needed
# tuple2=(10)
# print(type(tuple1))
# print(type(tuple2))

tuple3=(1,23,45,(6,10.12))
print(tuple3[0])
print(tuple3[3])

#nested tuple
tuple4=('turjo',"zahidul",'boss')
tuple5=(tuple3,tuple4)
print(tuple5)

list=[1.2,345,56,23]
print(tuple(list))