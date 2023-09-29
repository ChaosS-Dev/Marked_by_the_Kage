# Pong Project

import turtle

wn = turtle.Screen()
wn.title("Bingo Bongo :)")
wn.bgcolor("Black")
wn.setup(width=800, height=600)
wn.tracer(0)


# Score

score_1 = 0
score_2 = 0


# Player 1

p1 = turtle.Turtle()
p1.speed(0)
p1.shape("square")
p1.color("purple")
p1.shapesize(stretch_wid=8, stretch_len=1)
p1.penup()
p1.goto(-350, 0)


def p1_up():
    y = p1.ycor()
    if y <= 200:
        y += 20
        p1.sety(y)
    else:
        y += 0
        p1.sety(y)


def p1_down():
    y = p1.ycor()
    if y >= -200:
        y -= 20
        p1.sety(y)
    else:
        y -= 0
        p1.sety(y)

# Player 2


p2 = turtle.Turtle()
p2.speed(0)
p2.shape("square")
p2.color("purple")
p2.shapesize(stretch_wid=8, stretch_len=1)
p2.penup()
p2.goto(350, 0)


def p2_up():
    y = p2.ycor()
    if y <= 200:
        y += 20
        p2.sety(y)
    else:
        y += 0
        p2.sety(y)


def p2_down():
    y = p2.ycor()
    if y >= -200:
        y -= 20
        p2.sety(y)
    else:
        y -= 0
        p2.sety(y)


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center",
          font=("Courier", 24, "bold"))

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("purple")
ball.penup()
ball.goto(0, 0)

ball.dx = 0.2
ball.dy = 0.2


# Keyboard

wn.listen()
wn.onkeypress(p1_up, "w")
wn.onkeypress(p1_down, "s")

wn.onkeypress(p2_up, "Up")
wn.onkeypress(p2_down, "Down")


# Main game loop
while True:
    wn.update()


# Ball movement

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


# Ball window colision + score

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_1, score_2),
                  align="center", font=("Courier", 24, "bold"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_1, score_2),
                  align="center", font=("Courier", 24, "bold"))


# Player 1 colision

    if ball.xcor() > 340 and ball.ycor() < (p2.ycor() + 50) and ball.ycor() > (p2.ycor() - 50):
        ball.dx *= -1

    if ball.xcor() < -340 and ball.ycor() < (p1.ycor() + 50) and ball.ycor() > (p1.ycor() - 50):
        ball.dx *= -1
