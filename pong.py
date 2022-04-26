import turtle

wn = turtle.Screen()
wn.title("Pong by @clxrity")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

## Score
score_a = 0
score_b = 0


## Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # Animation speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

## Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) # Animation speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350, 0)

## Ball
ball = turtle.Turtle()
ball.speed(0) # Animation speed
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
# Movement speed 
# (I recommend starting your speed at 2 or 1 and adjusting based on how fast it moves)
ball.dx = 0.1
ball.dy = 0.1

## Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Tahoma", 24, "normal"))

## Functions

# Paddle a move
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

# Paddle b move
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)    

## Keyboard binding
wn.listen()
# Paddle a (left)
wn.onkeypress(paddle_a_up, "w")    
wn.onkeypress(paddle_a_down, "s")
# Paddle b (right)
wn.onkeypress(paddle_b_up, "Up")    
wn.onkeypress(paddle_b_down, "Down")


### Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    ## Border checking
    # Top
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    # Bottom
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    # Right
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        # Score
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Tahoma", 24, "normal"))

    # Left
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        # Score
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Tahoma", 24, "normal"))


    ## Paddle & ball collisions

    # Paddle b (right)
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    # Paddle a (left)
    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1