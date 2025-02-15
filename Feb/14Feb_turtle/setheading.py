import turtle
import time

t=turtle.Turtle()
t.shape("arrow")
#bydefault direction is east
#upwarddirection , north
t.setheading(90)
time.sleep(1)
#backword, west direction
t.setheading(180)
time.sleep(1)
#downward direction, south
t.setheading(270)
time.sleep(1)

turtle.exitonclick()
