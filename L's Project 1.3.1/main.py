import turtle as trtl

wn = trtl.Screen()


def fwd(dist: float):
    letter.forward(dist)

def bkwd(dist: float):
    letter.backward(dist)

def right(angle: float):
    letter.right(angle)

def left(angle: float):
    letter.left(angle)

def penSwitch(turtle: trtl.Turtle, on: bool = False):
    if on == True:
        turtle.pendown()
    else:
        turtle.penup()





letter = trtl.Turtle()
question = trtl.Turtle(); question.hideturtle(); penSwitch(question)
drawing = trtl.Turtle(); drawing.hideturtle(); penSwitch(drawing)
letterFont = ["Courier", 11, "bold"]
questionFont = ["Arial", 23, "bold"]

letter.speed(8)
letter.pensize(6)
letter.hideturtle()
question.goto(-350, 150)
question.write("Hello! What's your name?", font=questionFont)

name = wn.textinput('Name', "What's your name?")

if name:
    question.clear()
    penSwitch(letter)
    letter.goto(-400, 300)
    penSwitch(letter, True)
    letter.color("pink")
    letter.begin_fill()
    fwd(825)
    right(90)
    fwd(575)
    right(90)
    fwd(825)
    right(90)
    fwd(575)
    letter.end_fill()
    penSwitch(letter)
    letter.goto(25, 300)
    letter.color("black")
    penSwitch(letter, True)
    right(180)
    fwd(575)
    penSwitch(letter)
    letter.goto(-400, 70)
    drawing.goto(100, 70)
    drawing.hideturtle()
    letter.write("Hey, " + name + "! " + "I hope you're having a great day!",font=letterFont)
    drawing.write("You're awesome! :D", font=questionFont)
else:
    question.color("red")
    question.clear()
    question.write("You must have a name! Come back soon!", font=questionFont)
    wn.bye()

wn.mainloop()
