class Student:
    def __init__(self,name,roll,age) -> None:
        self.name=name
        self._roll=roll
        self.__age=age
    def get_age(self):
        return self.__age    
    def set_age(self,age):
        self.__age=age
    def display(self):
        print(f"hi i am {self.name}")  
        print(f"my age is {self.__age}")  
class Branch(Student):
    pass
# b1=Branch("turjo",1,22)
#
# s1=Student('Turjo',2,22)
# print(s1.get_age())
# s1.display()
# print("after setter method")
# s1.set_age(34)
# print(s1.get_age())
# s1.display()
b=Branch("turj0",1,22)
print(b.get_age())
b.display()
