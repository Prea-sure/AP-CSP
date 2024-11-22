# Turtle Escape (a124)
import turtle as trtl
import random as rand

# maze configuration variables
num_sides = 25
path_width = 15 
wall_color = "black"

def draw_door(pos):
  maze_drawer.forward(pos)
  maze_drawer.penup()
  maze_drawer.forward(path_width * 2)
  maze_drawer.pendown()

def draw_barrier(pos):
  maze_drawer.forward(pos)
  maze_drawer.left(90)
  maze_drawer.forward(path_width * 2)
  maze_drawer.backward(path_width * 2)
  maze_drawer.right(90)

def Up():
  mazeRunner.seth(90)

def Down():
  mazeRunner.seth(-90)

def Right():
  mazeRunner.seth(0)

def Left():
  mazeRunner.seth(-180)

def Move():
  mazeRunner.forward(90)
# init screen
wn = trtl.Screen()

# config maze
maze_drawer = trtl.Turtle()
maze_drawer.pensize(5)
maze_drawer.pencolor(wall_color)
maze_drawer.speed("fastest")

# draw maze from the middlle out
wall_len = path_width
for w in range(num_sides): 
  wall_len += path_width

  if (w > 5): 
    maze_drawer.left(90)

    door = rand.randint(path_width * 2, (wall_len - path_width * 2))
    barrier = rand.randint(path_width * 2, (wall_len - path_width * 2))

    while abs(door - barrier) < path_width:
        door = rand.randint(path_width * 2, (wall_len - path_width * 2))

    if (door < barrier):
      draw_door(door)
      draw_barrier(barrier - door - path_width * 2)
      maze_drawer.forward(wall_len - barrier)
    else: 
      draw_barrier(barrier)
      draw_door(door - barrier)
      maze_drawer.forward(wall_len - door - path_width*2)

maze_drawer.hideturtle()

mazeRunner = trtl.Turtle()
shapes = ["circle", "triangle", "square", "arrow", "turtle"]
mazeRunner.up()
mazeRunner.goto(-75, 50)
mazeRunner.shape(rand.choice(shapes))

wn.onkeypress(Up, "w")
wn.onkeypress(Left, "a")
wn.onkeypress(Down, "s")
wn.onkeypress(Right, "d")
wn.onkeypress(Move, "g")
wn.listen()
wn.mainloop()
