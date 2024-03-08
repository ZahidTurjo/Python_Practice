class Human:
    def __init__(self,name) -> None:
        self.name=name
    def eat(self):
        print(f"{self.name } can eat")
class Male(Human):
    def sleep(self):
        print("i can sleep whole day") 

class Female(Human):
    
    def work(self):
        print("I can code")
        

male_1=Male("turjo")
female_1=Female('rafiyat')
male_1.sleep()               
print(male_1.name)
male_1.eat()
female_1.eat()