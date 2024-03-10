# print(int.__add__(1,2))
# print(str.__add__("1","2"))
# class complexNumber:
#     def __init__(self,r,i) -> None:
#         self.real=r
#         self.imaginary=i
#     def __add__(self,other):
#         return f"{self.real+other.real}+{self.imaginary+other.imaginary}i"
# c1=complexNumber(1,2)
# c2=complexNumber(4,5)
# print(c1+c2)        \
class Person:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
    def __gt__(self,other):
        return self.age>other.age
        
p1=Person("turjo",22)
p2=Person("zahid",23)
print(p1>p2)
if p1>p2:
    print(f"{p1.name} will pay the bill")
else:
    print(f'{p2.name} will pay the bill')            
        
