
from turtle import Turtle,Screen
import random
color_list=['blue','green',"black","yellow","orange","gray","khaki"]
s1=Screen()
tom=Turtle()

tom.speed(3)
tom.shape("turtle")
# for i in range(5):
#     tom.forward(100)
#     tom.left(72)

for i in range(3,100):
    angle=360/i
    color=random.choice(color_list)
   
    for j in range(i):
        tom.pencolor(color)
        tom.forward(100)
        tom.left(angle)

s1.mainloop()