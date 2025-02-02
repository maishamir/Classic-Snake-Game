import turtle
import time
import random

delay = 0.1

# set up screen
wn = turtle.Screen()
wn.title("Snake game!")
wn.bgcolor("coral")
wn.setup(width=600, height=600)
wn.tracer(0) #turns off animation on screen

# snake head
head = turtle.Turtle()
head.speed(0) # animation speed of turtle module (fastest speed)
head.shape("square")
head.color("darkblue")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food    
food = turtle.Turtle()
food.speed(0) # animation speed of turtle module (fastest speed)
food.shape("square")
food.shapesize(0.5, 0.5)
food.color("white")
food.penup()
food.goto(0, 100)

segments = []

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

# keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)
# Main game loop
while True:
    wn.update() # updates the screen

    # Check for a collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        
        # hide the segments
        for segment in segments:
            segment.goto(1000,1000)

        # clear the segments list
        segments.clear()

    time.sleep(delay)

    # Check for a collision with the food
    if head.distance(food) < 20:
        # move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # Add a segment
        new_seg = turtle.Turtle()
        new_seg.speed(0)
        new_seg.shape("square")
        new_seg.color("lightblue")
        new_seg.penup()
        segments.append(new_seg )

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
             # hide the segments
            for segment in segments:
                segment.goto(1000,1000)

            # clear the segments list
            segments.clear()


wn.mainloop() #keeps window open