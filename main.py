import turtle as trtl
import random as rand
from time import *


def wait(sec: float):
    sleep(sec)


robot_idle = "robot-idle.gif"
robot_run = "robot-run.gif"

font = ("Futura", 13, "bold")

wn = trtl.Screen()
text = trtl.Turtle()
robot = trtl.Turtle()
wn.addshape(robot_idle)
wn.addshape(robot_run)
wn.title("Test Your Math")


robot.resizemode("auto")
robot.shape(robot_idle)

robot.hideturtle()
robot.penup()
robot.goto(robot.xcor() + 270, robot.ycor() + 210)
robot.showturtle()


text.hideturtle()
text.penup()
text.goto(text.xcor() - 220, text.ycor() + 200)
text.write("Hello user! What is your name?", font=font)


question: float
user = wn.textinput("Username", "User:")



if user:
    text.clear()
    text.write("Welcome " + user + "! " + "Are you ready to do some basic math?", font=font)
    yesNo = wn.textinput("Are you ready?", "Yes or No")
    if yesNo == "yes" or yesNo == "Yes" or yesNo == "Y" or yesNo == "y":
        text.clear()
        text.write("Alright! Let's begin!", font=font)
        text.clear()
        question = wn.numinput("Question", "What is " + str(rand.randint(1, 20)) + " + " + str(rand.randint(1, 20)) + "?")
        while 
    else:
        text.clear()
        text.write("Oh. Well, goodbye!", font=font)
        wait(1.5)
        wn.bye()




wn.mainloop()
