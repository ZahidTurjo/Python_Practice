class Human:
    def __init__(self,heart) -> None:
        self.num_eyes=2
        self.num_nose=1
        self.num_heart=heart
    def eat(self):
        print(self)
        print("I can eat")
    def work(self):
        print("I can work")
class Male(Human):
    def __init__(self,name,heart) -> None:
        self.name=name
        self.eye_color="green"
        super().__init__(heart)
    def run(self):
        print(self)
        return("i can run")
    def display(self):
        print(f"i am {self.name}")
male_1=Male("turjo",10)
print(male_1.num_eyes)        
print(male_1.eye_color)
print(male_1.name)
print(male_1.num_heart)
male_1.display()