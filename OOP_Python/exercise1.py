import math
class CircleArea:
    def __init__(self,radius):
        self.radius=radius
    def circle_area(self):
        return math.pi*self.radius**2
        

x=int(input("enter the radius of a circle:"))
circleArea_1=CircleArea(x)    
area=circleArea_1.circle_area()
print(f"area of a circle {area}")

# area of a rectangle--->

class Rectangle:
    def __init__(self,height,width):
        self.height=height
        self.width=width
    def rectangle_area(self):
        return self.height*self.width    

a=int(input("enter the height: "))
b=int(input("enter the width:"))

rectangle_1=Rectangle(a,b)
area=rectangle_1.rectangle_area()
print(f"area of a rectangle {area}")


