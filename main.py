import turtle as trtl
import random as rand
from time import *


def wait(sec: float):
    sleep(sec)

def goodbye():
    text.clear()
    text.write("Goodbye! Thanks for playing", font=font)


robot_idle = "robot-idle.gif"
robot_run = "robot-run.gif"
correct_mark = "correct.gif"
incorrect_mark = "incorrect.gif"

font = ("Futura", 13, "bold")
a = rand.randint(1, 20)
b = rand.randint(1, 20)


wn = trtl.Screen()
text = trtl.Turtle()
robot = trtl.Turtle()
correct = trtl.Turtle(); correct.penup()
incorrect = trtl.Turtle(); incorrect.penup()
wn.addshape(robot_idle)
wn.addshape(robot_run)
wn.addshape(correct_mark)
wn.addshape(incorrect_mark)
wn.title("Test Your Math")


correct.hideturtle(); correct.goto(correct.xcor() - 270, correct.ycor())
incorrect.hideturtle(); incorrect.goto(incorrect.xcor() + 270, incorrect.ycor() - 40)

correct.shape(correct_mark)
incorrect.shape(incorrect_mark)
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
        question = wn.numinput("Question", "What is " + str(a) + " + " + str(b) + "?")
        while True:
            if a + b != question:
                text.write("That's incorrect! " + str(a) + " + " + str(b) + " is " + str(a + b) + ". " + "Try again!", font=font)
                incorrect.showturtle()
                wait(2)
                incorrect.hideturtle()
                a = rand.randint(1, 20)
                b = rand.randint(1, 20)
                question = wn.numinput("Question", "What is " + str(a) + " + " + str(b) + "?")
                text.clear()
            else:
                text.write("That's correct! Good job.", font=font)
                correct.showturtle()
                wait(2)
                correct.hideturtle()
                a = rand.randint(1, 20)
                b = rand.randint(1, 20)
                question = wn.numinput("Question", "What is " + str(a) + " + " + str(b) + "?")
                text.clear()

    else:
        text.clear()
        text.write("Oh. Well, goodbye!", font=font)
        wait(1.5)
        wn.bye()
else:
    text.clear()
    text.write("You must have a name!", font=font)
    wait(1)
    wn.bye()


wn.onkeypress(goodbye, "y")
wn.mainloop()
