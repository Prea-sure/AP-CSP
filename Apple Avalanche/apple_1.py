#   a123_apple_1.py
import turtle as trtl
import random as rand

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
pear_image = "pear.gif"
overlay_font = ("Arial", 43, "bold")
random_letters = ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";", "'", "Enter"]

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.addshape(pear_image)
wn.bgpic("background.gif")

apple = trtl.Turtle()
apple.up()
current_letter = rand.choice(random_letters)
#-----functions-----
def move_apple():
  x = apple.xcor()
  y = apple.ycor()
  apple.clear()
  apple.goto(x, y - wn.canvheight / 2)
  apple.hideturtle()
  reset_apple(apple)

# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple: trtl.Turtle, letter: str, image=apple_image):
  active_apple.shape(image)
  wn.update()
  letter_overlay(letter, active_apple)
 

def letter_overlay(letter: str, current_apple: trtl.Turtle):
  current_apple.color("white")
  current_apple.showturtle()
  current_apple.write(letter, align="center", font=overlay_font)
  current_apple.setpos(apple.xcor(), apple.ycor() + 40)


def reset_apple(current_apple: trtl.Turtle):
  global current_letter, random_letters
  random_len = len(random_letters)
  if random_len != 0:
    randomX = rand.randint(-wn.canvwidth / 2, wn.canvwidth / 2)
    randomY = rand.randint(-wn.canvheight / 2, wn.canvheight / 2)
    current_apple.goto(randomX, randomY)
    current_letter = rand.choice(random_letters)
    draw_apple(current_apple, current_letter)

def checkA():
  if current_letter == "A":
    move_apple()

def checkS():
  if current_letter == "S":
    move_apple()

def checkD():
  if current_letter == "D":
    move_apple()

def checkF():
  if current_letter == "F":
    move_apple()

def checkG():
  if current_letter == "G":
    move_apple()

def checkH():
  if current_letter == "H":
    move_apple()

def checkJ():
  if current_letter == "J":
    move_apple()

def checkK():
  if current_letter == "K":
    move_apple()

def checkL():
  if current_letter == "L":
    move_apple()

def checkSemiColon():
  if current_letter == ";":
    move_apple()

def checkSingleQuote():
  if current_letter == "'":
    move_apple()

def checkEnter():
  if current_letter == "Enter":
    move_apple()
#-----function calls-----
draw_apple(apple, current_letter)

wn.onkeypress(checkA, "a")
wn.onkeypress(checkS, "s")
wn.onkeypress(checkD, "d")
wn.onkeypress(checkF, "f")
wn.onkeypress(checkG, "g")
wn.onkeypress(checkH, "h")
wn.onkeypress(checkJ, "j")
wn.onkeypress(checkK, "k")
wn.onkeypress(checkL, "l")
wn.onkeypress(checkSemiColon, ";")
wn.onkeypress(checkSingleQuote, "'")
wn.onkeypress(checkEnter, "Return")
wn.listen()
wn.mainloop()