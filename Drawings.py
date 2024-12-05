# Python program that allows you (the user) to create their own drawings and polygons with key-binded functions and their cursor. Images drawn can also be saved to their files.
import turtle as trtl
from time import *


# Turtle setup, screen setup
turtle = trtl.Turtle()
wn = trtl.Screen()
ts = turtle.getscreen()
cv = ts.getcanvas()
# Key binds list
keybinds = ["z", "e", "t", "u", "r", "Return", "v", "p", "q"]
# Helper functions/User-input functions

# Pauses program execution for s amount of seconds. (Wrapper function for time.sleep())
def wait(seconds: float | int):
    sleep(seconds)

# Moves turtle to location of cursor on screen.
def goto(x, y):
    turtle.goto(x, y)

# Creates a square with radius and extent.
def square(rad: float, extent: float):
    turtle.circle(rad, extent, 4)

# Creates a triangle with radius and extent.
def triangle(rad: float, extent: float):
    turtle.circle(rad, extent, 3)

# Creates custom polygon based on radius, extent, and steps.
def customPoly():
    rad, extent, steps = input("What would you like the radius, extent, and steps of your polygon to be? [No Commas] ").split()
    turtle.circle(float(rad), float(extent), int(steps))

# Undoes last action from turtle/cursor.
def undo():
    turtle.undo()

# Hides turtle icon.
def hideTurtle():
    turtle.hideturtle()

# Shows turtle icon.
def showTurtle():
    turtle.showturtle()

# Disables drawing for turtle.
def penUp():
    turtle.penup()

# Reenables drawing for turtle.
def penDown():
    turtle.pendown()


def penColor():
    color = input("What color would you like to change the pen to? ")
    turtle.pencolor(color)

def penSize():
    size = int(input("How thick would you like the pen to be? "))
    turtle.pensize(size)

# Gets input for shape of user input, and creates it based on cases.
def getShapeInput():
    shapeInput: str = input("What shape would you like to create? ")
    match shapeInput:
        case "square":
            rad, extent = input("What would you like the radius and the extent of the square to be? [No Commas] ").split()
            square(float(rad), float(extent))
        case "triangle":
            rad, extent = input("What would you like the radius and extent of the triangle to be? [No Commas] ").split()
            triangle(float(rad), float(extent))
        case "custom":
            customPoly()

# Saves the drawing to a .ps file which can be viewed online.
def finishedDrawing():
    fileName = input("What would you like to name this drawing? ")
    print("Nice drawing!", fileName, "will be saved as a .ps file on your computer. You can view on https://psviewer.org/onlineviewer.aspx")
    cv.postscript(file=fileName + ".ps", colormode="color", width=1000, height=1000)
    turtle.penup()
    turtle.clear()
    
# Get username
name = input("Hello user! What is your name? ")

# Dialogue/Main sequence
if name:
    print("Well hello,", name + "!")
    wait(1)
    creation = input("What would you like to create? ")
    wait(1)
    print("A", creation + "?", "Cool! Let's see if you have the skills to make it.")
    wait(1)
    print("CONTROLS:\n", "LMB - Moves mouse to cursor\n","Z - Undo [PERMANENT]\n", "E - Hide Turtle\n", "V - Show Turtle\n", "T - Penup\n", "U - Pendown\n", "R - Create Shape (Prompt)\n","P - Change Pen Color\n", "Q - Change Pen Size\n", "Enter - Finish drawing")
    wait(3)
    print("The only defined shapes are squares and triangles, but you can make your own custom polygon.")
    wait(1)
    print("Have fun!")



# Cursor/key events + listener
ts.onclick(goto)
ts.onkey(undo, keybinds[0])
ts.onkey(hideTurtle, keybinds[1])
ts.onkey(penUp, keybinds[2])
ts.onkey(penDown, keybinds[3])
ts.onkey(getShapeInput, keybinds[4])
ts.onkey(finishedDrawing, keybinds[5])
ts.onkey(showTurtle, keybinds[6])
ts.onkey(penColor, keybinds[7])
ts.onkey(penSize, keybinds[8])
ts.listen()
ts.mainloop()





