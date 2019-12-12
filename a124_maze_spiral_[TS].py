#import turtle
import turtle as trtl 
#import random
import random
runner = trtl.Turtle()
player = trtl.Turtle()
#Detailize turtle
runner.pensize(5)
runner.pencolor("purple")
runner.speed(0)

#detailize other turtle
player.pensize(7)
player.color("orange")
player.up()

#create color list
cool_colors = ["red", "orange", "brown", "orchid", "green", "blue", "purple"]


# wall variables
#starting wall length
wall_length = 45
#how much the wall length grows every new wall
wall_growth = 15
#How long the last wall is
final_wall_length = 150
#the size of the gaps 
gapsize = 20
#the length of the barriers
barrier_length = 25 
num_walls = 25




# make turtle start at (0,0) and face up
runner.up()
runner.goto(0,0)
runner.down()
runner.setheading(90)

player.up()
player.goto(175, 230)

def drawBarrier():

    runner.left(90)
    runner.forward(barrier_length)
    runner.left(180)
    runner.forward(barrier_length)
    runner.left(90)

def drawDoor():
    runner.up()
#make the gaps
    runner.forward(gapsize)
    runner.down()


#draw the maze
while num_walls > 0:
    door = random.randint(gapsize, wall_length - gapsize)
    barrier = random.randint(gapsize, wall_length - gapsize)
    
    
    if gapsize < barrier_length:
        
        runner.forward(door)
        drawDoor()
        runner.forward(barrier - door - gapsize)
        drawBarrier()
        runner.forward(wall_length - barrier)

    else:
        runner.forward(barrier)
        drawBarrier()
        runner.forward(door - barrier)
        drawDoor()
        runner.forward(wall_length - door - gapsize)
    
    runner.pencolor(random.choice(cool_colors))
    runner.left(90)
    wall_length = wall_length + wall_growth
    num_walls = num_walls - 1
'''def door_first():
    runner.down()
    runner.forward(gapsize)
    runner.up()
    runner.forward(gapsize)
    runner.forward(barrier_length - gapsize - gapsize)
    runner.left(90)
    runner.forward(wall_length - barrier_length)
    runner.back()
    runner.left(90)'''


def Up():
    player.setheading(90)
    player.forward(10)

def Left():
    player.setheading(180)
    player.forward(10)

def Right():
    player.setheading(0)
    player.forward(10)

def Down():
    player.setheading(270)
    player.forward(10)

wn = trtl.Screen()
wn.onkeypress(Up,"Up")
wn.onkeypress(Left, "Left")
wn.onkeypress(Right, "Right")
wn.onkeypress(Down, "Down")
wn.listen()
wn.mainloop()