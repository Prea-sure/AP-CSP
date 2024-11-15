#   a123_apple_1.py TEST VERSION [UNFINISHED]
import turtle as trtl
import random as rand

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
pear_image = "pear.gif"
overlay_font = ("Arial", 43, "bold")
random_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.addshape(pear_image)
wn.bgpic("background.gif")



apples = []
for i in range(5):
  apple = trtl.Turtle()
  apple.hideturtle()
  apple.penup()
  apple.showturtle()
  apples.append(apple)
  
for apple in apples:
  apple.goto(rand.randint(-wn.canvwidth / 2.5, wn.canvwidth / 2.5), rand.randint(-wn.canvheight / 2.5, wn.canvheight / 2.5))
 

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
    current_apple.setpos(current_apple.xcor(), current_apple.ycor() + 40)


def reset_apple(current_apple: trtl.Turtle):
  random_len = len(random_letters)
  if random_len != 0:
    randomX = rand.randint(-wn.canvwidth / 2.5, wn.canvwidth / 2.5)
    randomY = rand.randint(-wn.canvheight / 2.5, wn.canvheight / 2.5)
    current_apple.goto(randomX, randomY)
    current_letter = rand.choice(random_letters)
    print(current_letter)
    draw_apple(current_apple, current_letter)
    random_letters.remove(current_letter)
    print(random_letters)
    

# TODO: Make this more efficient [in like a year]
def checkA():
  if current_letter == "A":
    move_apple()

def checkB():
  if current_letter == "B":
    move_apple()

def checkC():
  if current_letter == "C":
    move_apple()

def checkD():
  if current_letter == "D":
    move_apple()

def checkE():
  if current_letter == "E":
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

def checkI():
  if current_letter == "I":
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

def checkM():
  if current_letter == "M":
    move_apple()

def checkN():
  if current_letter == "N":
    move_apple()

def checkO():
  if current_letter == "O":
    move_apple()

def checkP():
  if current_letter == "P":
    move_apple()

def checkQ():
  if current_letter == "Q":
    move_apple()

def checkR():
  if current_letter == "R":
    move_apple()

def checkS():
  if current_letter == "S":
    move_apple()

def checkT():
  if current_letter == "T":
    move_apple()

def checkU():
  if current_letter == "U":
    move_apple()

def checkV():
  if current_letter == "V":
    move_apple()

def checkW():
  if current_letter == "W":
    move_apple()

def checkX():
  if current_letter == "X":
    move_apple()

def checkY():
  if current_letter == "Y":
    move_apple()

def checkZ():
  if current_letter == "Z":
    move_apple()


#-----function calls-----
for apple in apples:
  if current_letter != rand.choice(random_letters):
    current_letter = rand.choice(random_letters)
    draw_apple(apple, current_letter)

wn.onkeypress(checkA, "a")
wn.onkeypress(checkB, "b")
wn.onkeypress(checkC, "c")
wn.onkeypress(checkD, "d")
wn.onkeypress(checkE, "e")
wn.onkeypress(checkF, "f")
wn.onkeypress(checkG, "g")
wn.onkeypress(checkH, "h")
wn.onkeypress(checkI, "i")
wn.onkeypress(checkJ, "j")
wn.onkeypress(checkK, "k")
wn.onkeypress(checkL, "l")
wn.onkeypress(checkM, "m")
wn.onkeypress(checkN, "n")
wn.onkeypress(checkO, "o")
wn.onkeypress(checkP, "p")
wn.onkeypress(checkQ, "q")
wn.onkeypress(checkR, "r")
wn.onkeypress(checkS, "s")
wn.onkeypress(checkT, "t")
wn.onkeypress(checkU, "u")
wn.onkeypress(checkV, "v")
wn.onkeypress(checkW, "w")
wn.onkeypress(checkX, "x")
wn.onkeypress(checkY, "y")
wn.onkeypress(checkZ, "z")


wn.listen()
wn.mainloop()