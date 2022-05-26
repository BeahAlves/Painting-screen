from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def move_forwards():
    t.forward(10)


def move_right():
    t.right(5)


def move_left():
    t.left(5)


def backwards():
    t.back(10)


def clean():
    t.reset()


screen.onkeypress(move_right, 'd')
screen.onkeypress(move_forwards, 'w')
screen.onkeypress(move_left, 'a')
screen.onkeypress(backwards, 's')
screen.onkey(clean, 'c')
screen.listen()


screen.exitonclick()
