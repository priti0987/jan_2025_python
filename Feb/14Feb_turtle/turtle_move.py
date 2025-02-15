import time
import turtle

# t=turtle.Turtle()
# t.shape("circle")
# t.shapesize(5)
# time.sleep(1)
# t.forward(100)
# time.sleep(1)
# t.backward(80)
# time.sleep(1)
# t.right(45)
# time.sleep(1)
# t.left(25)
# time.sleep(1)
# t.back(90)
# #draw square

t1=turtle.Turtle()
t1.shape("arrow")
t1.shapesize(5)
t1.setheading(20)

for i in range(4):
    t1.forward(100)
    t1.right(90)

turtle.exitonclick()