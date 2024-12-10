import turtle as trtl
from time import *


turtle = trtl.Turtle()
wn = trtl.Screen()
wn.bgcolor("black")

font = ("Futura", 20, "bold")

turtle.hideturtle()
turtle.pencolor("white")
turtle.penup()
turtle.goto(turtle.xcor() - 30, turtle.ycor() + 200)
turtle.write("test", font=font)




wn.mainloop()