# For Leslie
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

def penSwitch(on: bool = False):
    if on == True:
        letter.pendown()
    else:
        letter.penup()





letter = trtl.Turtle()
font = ["Courier", 10, "normal"]
letter.speed(8)
letter.pensize(6)
letter.hideturtle()
penSwitch()
letter.goto(-400, 300)
penSwitch(True)
letter.color("pink")
letter.begin_fill()
fwd(725)
right(90)
fwd(475)
right(90)
fwd(725)
right(90)
fwd(475)
letter.end_fill()
penSwitch()
letter.goto(-30, 300)
letter.color("black")
penSwitch(True)
right(180)
fwd(475)
penSwitch()
letter.goto(-50, 0)
letter.write("",font=font)

wn.mainloop()