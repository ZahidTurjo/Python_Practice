# method overloading_____________>>-->>
 
#class Calculator:
#     def add(self,*args):
#         if len(args) == 2:
#             return args[0]+args[1]
#         elif len(args) == 3:
#             return args[0]+args[1]+args[2]
# cal=Calculator()
# print(cal.add(1,2))        
# print(cal.add(1,2,3))

# class Demo:
#     def add(self,a,b,c):
#         return a+b+c
#     def add(self,a,b):
#         return a+b
    
# d=Demo()    
# print(d.add(1,2))
# print(d.add(1,2,3))

# method overriding__>><<<---->>>__
class Person:
    def speaks(self):
        print("Person can speak")
class Male(Person):
    def speaks(self):
        print("male can speak")
        # super().speaks()        
m=Male()
p=Person()
m.speaks()
p.speaks()
        