import turtle 

painter = turtle.Turtle()

painter.pencolor("red")

for i in range(100):
    painter.forward(50)
    painter.left(123) 
    
painter.pencolor("black")
for i in range(100):
    painter.forward(100)
    painter.left(123)
    
turtle.done()