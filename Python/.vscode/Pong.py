import turtle

wn = turtle.Screen()
wn.title("Pong :)")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


# Player 1
player_1 = turtle.Turtle()
player_1.speed(0)   # velocidade da animação
player_1.shape("square")
player_1.color("white")
player_1.shapesize(stretch_wid=5, stretch_len=1)
player_1.penup()
player_1.goto(-350, 0)  # coordenadas


# Player 2
player_2 = turtle.Turtle()
player_2.speed(0)   # velocidade da animação
player_2.shape("square")
player_2.color("white")
player_2.shapesize(stretch_wid=5, stretch_len=1)
player_2.penup()
player_2.goto(350, 0)  # coordenadas


# Ball
ball = turtle.Turtle()
ball.speed(0)   # velocidade da animação
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)  # coordenadas

ball.dx = 0.5  # "A cada instante a bola move 2 x"
ball.dy = 0.2

# Functions


def player_1_up():
    y = player_1.ycor()
    y += 20
    player_1.sety(y)


def player_1_down():
    y = player_1.ycor()
    y -= 20
    player_1.sety(y)


def player_2_up():
    y = player_2.ycor()
    y += 20
    player_2.sety(y)


def player_2_down():
    y = player_2.ycor()
    y -= 20
    player_2.sety(y)


# Keyboard
wn.listen()

wn.onkeypress(player_1_up, "w")
wn.onkeypress(player_1_down, "s")

wn.onkeypress(player_2_up, "Up")
wn.onkeypress(player_2_down, "Down")


# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)  # Loop do movimento da bola
    ball.sety(ball.ycor() + ball.dy)
