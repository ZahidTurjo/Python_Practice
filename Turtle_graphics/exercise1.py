from turtle import Turtle,Screen
s1=Screen()
tom=Turtle()

for i in range(10):
    # tom.pencolor("red")
    tom.forward(10)
    tom.penup()
    tom.forward(10)
    tom.pendown()
    
    # tom.forward(10)
    # tom.penup()
s1.mainloop()