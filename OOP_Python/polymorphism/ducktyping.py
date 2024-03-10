class Duck:
    def swim(self):
        print("I am duck and i can swim")
    def speaks(self):
        print("Quack Quack")    
class Dog:
    def swim(self):
        print("I am dog and I can swim ")
    def speaks(self):
        print("Woof Woof")
class Person:
    def speaks(slef):
        print("Bla Bla Bla")        


def display(object):
    object.swim()
    object.speaks()
    print("Information Displayed")
duck= Duck()  
dog=Dog() 
person=Person()
 
display(duck)   
display(dog)   
display(person)                  