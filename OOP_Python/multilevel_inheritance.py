class Human:
    def __init__(self,language) -> None:
        self.num_eyes=2
        self.num_nose=1
        self.language=language
    def eat(self):
        print('i can eat')
    def work(self):
        print("i can work")      
class Male(Human):
    def __init__(self,brain) -> None:
        self.brain=brain
        
        
    def sleep(self):
        print("I can sleep whole day")
    def work(self):
        print("I can code")     

class Boy(Male):
    def __init__(self,name,brain,language) -> None:
        self.name=name
        Male.__init__(self,brain)
        Human.__init__(self,language)

    def work(self):
        print("I can test")
        Human.work(self)
        super().work()
        
boy_1=Boy('Turjo',"brain",'python')
print(boy_1.num_eyes)
print(boy_1.name)
print(boy_1.brain)
print(boy_1.language)
           