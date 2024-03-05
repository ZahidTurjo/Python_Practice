class Instructor:
    def __init__(self,name,address,):
        self.name=name
        self.address=address     
        self.followrs=0
        
instructor_1=Instructor("turjo","dhaka")

print(instructor_1.name)


instructor_2=Instructor("Zahid",'Gazipur')
print(instructor_2.name)
print(instructor_2.followrs)
# instructor_2.name="Zahid"
# instructor_2.address="Dhaka"