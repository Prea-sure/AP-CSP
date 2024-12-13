import turtle as trtl
from time import *


def wait(sec: float):
    sleep(sec)

robot_sprite = "robot-idle.gif"
font = ("Futura", 16, "bold")

wn = trtl.Screen()
text = trtl.Turtle()
robot = trtl.Turtle()
wn.addshape(robot_sprite)
wn.title("Test Your Math")



robot.resizemode("auto")
robot.shape(robot_sprite)
robot.hideturtle()
robot.penup()
robot.goto(robot.xcor() + 270, robot.ycor() + 210)
robot.showturtle()

text.hideturtle()
text.penup()
text.goto(text.xcor() - 220, text.ycor() + 200)
text.write("Hello user! What is your name?", font=font)

user = wn.textinput("Username", "User:")

if user:
    text.clear()
    text.write("Welcome", user + "!", "Are you ready to do some basic math?")
    yesNo = wn.textinput("Are you ready?", "Yes or No")
    if yesNo == "yes":
        text.clear()



wn.mainloop()