class Instructor:
    followers=0
    def __init__(self,name,address):
        self.name=name
        self.address=address
    def display(self,subject):
        print(subject)
        return f"Hi {self.name}"
    def update_followers(self):
        print(self.name)
        self.followers+=1
   
  

instructor_1=Instructor("turjo","Dhaka")    
print(instructor_1.display('Python'))
instructor_1.update_followers()
print(instructor_1.followers)
instructor_1.update_followers()
print(instructor_1.followers)