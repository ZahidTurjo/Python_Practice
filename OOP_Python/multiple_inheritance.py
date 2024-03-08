class Human:
    def __init__(self,brain):
        print("caling from human")
        self.num_eyes=2
        self.num_nose=1
        self.brain=brain
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class Male:
    def __init__(self,name,) -> None:
        print("Calling from Male")
        self.name=name   
    def flirt(self):
        print("I can flirt")
    def work(self):
       
        print("I can code")
class Boy(Human,Male):
    def __init__(self,name,brain,language):
        self.language=language
        Male.__init__(self,name)  #for calling the male class
        super().__init__(brain)   #super() call the base class
        
    def work(self):
        super().work()
        Male.work(self)
        print("i can test")
    def display(self):
        print(f"hi i am {self.name} and i am speaking in {self.language}")
        
boy_1=Boy("turjo","brain","french")
print(boy_1.num_eyes)
print(boy_1.name)
print(boy_1.brain)
print(boy_1.language)
boy_1.display()
              