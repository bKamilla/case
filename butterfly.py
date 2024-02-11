import turtle
#beginning
screen = turtle.Screen()
t = turtle.Turtle()

#wings
t.begin_fill()
t.color('pink')
for i in range(3):
    t.forward(100)
    t.left(120)
t.end_fill()

t.left(60)
t.begin_fill()
t.color('brown')
t.circle(10)
t.end_fill()

t.circle(10,250)
t.begin_fill()
t.color('pink')
for i in range(3):
    t.backward(100)
    t.left(120)

t.left(70)
for i in range(3):
    t.backward(70)
    t.left(120)
t.end_fill()

t.up()
t.setposition(0,0)
t.down()
t.right(90)
t.begin_fill()
for i in range(3):
    t.forward(70)
    t.left(120)
t.end_fill()

#body
t.color('brown')
t.begin_fill()
t.right(110)
t.forward(7)
t.circle(10,540)
t.circle(-8,540)
t.circle(6,540)
t.circle(-3,540)
t.end_fill()
t.home()
t.left(60)
t.circle(10,120)
t.begin_fill()
t.circle(-9,540)
t.end_fill()

#tentacles
t.pencolor('black')
t.seth(90)
t.circle(60,50)
t.circle(10,180)
t.circle(5,160)
t.up()
t.setposition(-8.66,33.00)
t.down()
t.seth(80)
t.circle(-60,55)
t.circle(-10,180)
t.circle(-5,160)

#ending
screen.exitonclick()