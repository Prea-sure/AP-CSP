# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb
from time import *
wn = trtl.Screen()

#-----game configuration----
leaderboard_file_name = "a122_leaderboard.txt"
player_name = input("Hello user! What is your name? ")
beginningSize = 2
color = "pink"
shape = "circle"
score = 0
font_setup = ("Arial", 20, "normal")
timer = 5
times_up = False
ms = 1000
startTextFontSetup = ("Comic Sans", 20, "normal")

randomSizeList = [0.5, 0.6, 0.7, 0.8, 0.9, 1, 2, 3, 4, 5]
randomBgColor = ["green", "blue", "orange", "yellow", "white", "purple", "turquoise"]
#-----initialize turtle-----
dot = trtl.Turtle()
dot.shape(shape)
dot.shapesize(beginningSize) 
dot.color(color)

score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(0, 230)


counter = trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(-300, 230)


startText = trtl.Turtle()
startText.hideturtle()
startText.penup()
startText.goto(-50, -150)

#-----game functions--------
def manage_leaderboard():
    global score
    global dot

    leader_names_list = lb.get_names(leaderboard_file_name)
    leader_scores_list = lb.get_scores(leaderboard_file_name)

    if len(leader_scores_list) < 5 or score >= leader_scores_list[4]:
        lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
        lb.draw_leaderboard(True, leader_names_list, leader_scores_list, dot, score)
    else:
        lb.draw_leaderboard(False, leader_names_list, leader_scores_list, dot, score)

def countdown():
    global timer, times_up
    screen = counter.getscreen()
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up!", font=font_setup)
        times_up = True
        manage_leaderboard()
    else:
        counter.write("Time remaining: " + str(timer) + "s", font=font_setup)
        timer -= 1
        screen.ontimer(countdown, ms)

def change_position():    
    randomSize = rand.choice(randomSizeList)
    new_xpos = rand.randint(-200, 200)
    new_ypos = rand.randint(-150, 150)
    dot.penup()
    dot.hideturtle()
    dot.goto(new_xpos, new_ypos)
    dot.shapesize(randomSize)
    dot.showturtle()

def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write("Score: " + str(score), font=font_setup)
    
def onClick(x, y):
   global times_up
   if times_up == False:  
    change_position()
    update_score()
   else:
      dot.hideturtle()


def start_game():
    startText.write("Welcome to Catch-A-Turtle!", font=startTextFontSetup)
    sleep(1)
    startText.clear()
    startText.write("Are you ready to play? (Y/N)", font=startTextFontSetup)
    startInput = input("Are you ready to play? (Y/N) ")
    if startInput == "Y" or startInput == "y":
        startText.write("Good luck!", font=startTextFontSetup)
        sleep(0.5)
        startText.clear()
        dot.onclick(onClick)
        wn.ontimer(countdown, ms)
    else:
        dot.hideturtle()
        

#-----events----------------
start_game()
wn.bgcolor(rand.choice(randomBgColor))
wn.mainloop()




