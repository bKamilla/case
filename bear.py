import turtle
#beginning
screen = turtle.Screen()
t = turtle.Turtle()

#head
t.begin_fill()
t.color('brown')
t.circle(80)
t.end_fill()

t.begin_fill()
t.color('salmon3')
t.circle(40)
t.end_fill()

t.up()
t.circle(40,180)

t.begin_fill()
t.color('salmon')
t.circle(20)
t.end_fill()

t.up()
t.left(90)
t.forward(10)
t.left(90)
t.forward(50)
t.down()
t.color('black')
t.begin_fill()
t.circle(5)
t.end_fill()
t.up()
t.left(180)
t.forward(100)
t.down()
t.color('black')
t.begin_fill()
t.circle(-5)
t.end_fill()

#ears
t.up()
t.home()
t.circle(80,135)
t.down()
t.begin_fill()
t.color('brown')
t.circle(-38)
t.end_fill()
t.begin_fill()
t.color('salmon3')
t.circle(-28)
t.end_fill()

t.up()
t.home()
t.circle(80,-135)
t.down()
t.begin_fill()
t.color('brown')
t.circle(-38)
t.end_fill()
t.begin_fill()
t.color('salmon3')
t.circle(-28)
t.end_fill()

#body
t.up()
t.home()
t.down()
t.begin_fill()
t.color('brown')
t.circle(-100)
t.end_fill()
t.begin_fill()
t.color('salmon3')
t.circle(-85)
t.end_fill()

#limbs
t.up()
t.circle(-100,65)
t.down()
t.begin_fill()
t.color('brown')
t.forward(33)
t.left(90)
for i in range(3):
    t.forward(66)
    t.left(90)
t.forward(33)
t.end_fill()

t.up()
t.circle(-100,70)
t.down()
t.begin_fill()
t.color('brown')
t.forward(33)
t.left(90)
for i in range(3):
    t.forward(66)
    t.left(90)
t.forward(33)
t.end_fill()

t.up()
t.home()
t.circle(-100,-65)
t.down()
t.begin_fill()
t.color('brown')
t.forward(33)
t.left(90)
for i in range(3):
    t.forward(66)
    t.left(90)
t.forward(33)
t.end_fill()

t.up()
t.circle(-100,-70)
t.down()
t.begin_fill()
t.color('brown')
t.forward(33)
t.left(90)
for i in range(3):
    t.forward(66)
    t.left(90)
t.forward(33)
t.end_fill()




screen.exitonclick()