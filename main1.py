#robogirl
import turtle

def rectangle( a, b):
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.up()
    turtle.left(135)
    turtle.down()
    turtle.left(45)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(b)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(b)
    turtle.end_fill()

def rectangle1( a, b):
    turtle.fillcolor('pink')
    turtle.begin_fill()

    turtle.up()
    turtle.left(180)
    turtle.down()
    turtle.forward(b)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(b)
    turtle.right(90)
    turtle.forward(a)
    turtle.end_fill()

def rectangle2( a, b,c):
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.up()
    turtle.right(180)
    turtle.forward(c)
    turtle.left(90)
    turtle.down()
    turtle.forward(b)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(b)
    turtle.right(90)
    turtle.forward(a)
    turtle.end_fill()

def rectangle3( a, b,c):
    turtle.fillcolor('pink')
    turtle.begin_fill()
    turtle.up()
    turtle.forward(c)
    turtle.left(90)
    turtle.down()
    turtle.forward(b)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(b)
    turtle.right(90)
    turtle.forward(a)
    turtle.end_fill()

def trapezoid(x, y, a, b,c):
    turtle.fillcolor('blue')
    turtle.begin_fill()
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.forward(a)
    turtle.right(70)
    turtle.forward(c)
    turtle.right(110)
    turtle.forward(b)
    turtle.right(110)
    turtle.forward(c)
    turtle.end_fill()

def trapezoid1(x, y, a, b,c):
    turtle.fillcolor('green')
    turtle.begin_fill()
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.right(71)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(b)
    turtle.right(90)
    turtle.forward(c)
    turtle.setposition(x, y)
    turtle.end_fill()

def trapezoid2(x, y, a, b,c):
    turtle.fillcolor('green')
    turtle.begin_fill()
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(b)
    turtle.left(90)
    turtle.forward(c)
    turtle.setposition(x, y)
    turtle.end_fill()


#SHIP

def triangle(a,b):
    turtle.up()

    turtle.forward(200)
    turtle.left(90)
    turtle.forward(170)
    turtle.left(180)
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.down()
    turtle.forward(a)
    turtle.left(120)
    turtle.forward(b)
    turtle.left(120)
    turtle.forward(b)
    turtle.left(30)
    turtle.end_fill()


def triangle1(a, b):
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.up()
    turtle.forward(10)
    turtle.left(90)
    turtle.down()
    turtle.forward(a)
    turtle.right(120)
    turtle.forward(b)
    turtle.right(120)
    turtle.forward(b)
    turtle.right(30)
    turtle.end_fill()

def machta(a, b):
    turtle.fillcolor('black')
    turtle.begin_fill()

    turtle.forward(a)
    turtle.right(90)
    turtle.forward(b)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(b)
    turtle.end_fill()

def deck1(a, b):
    turtle.fillcolor('blue')
    turtle.begin_fill()
    turtle.up()
    turtle.right(180)
    turtle.forward(90)
    turtle.down()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(b)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(b)
    turtle.end_fill()

def deck2(a, b):
    turtle.fillcolor('blue')
    turtle.begin_fill()
    turtle.up()
    turtle.forward(10)
    turtle.down()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(b)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(b)
    turtle.end_fill()

def body(a, b,c,d):
    turtle.fillcolor('brown')
    turtle.begin_fill()
    turtle.up()
    turtle.right(180)
    turtle.forward(30)
    turtle.left(90)
    turtle.down()
    turtle.forward(a)
    turtle.right(150)
    turtle.forward(b)
    turtle.right(30)
    turtle.forward(c)
    turtle.right(30)
    turtle.forward(b)
    turtle.right(150)
    turtle.forward(d)
    turtle.end_fill()

def triangle2(a,b):
    turtle.up()

    turtle.left(90)
    turtle.forward(70)
    turtle.left(180)
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.down()
    turtle.forward(a)
    turtle.left(120)
    turtle.forward(b)
    turtle.left(120)
    turtle.forward(b)
    turtle.left(30)
    turtle.end_fill()
    turtle.left(90)


rectangle(10, 40)
rectangle1(100, 60)
rectangle2(10,40,100)
rectangle3(20,10,40)
trapezoid(20, -10, 60, 128,100)
trapezoid1(20, -104, 20, 50,40)
trapezoid2(80, -104, 20, 50,40)
triangle(50,50)
triangle1(50,50)
machta(10,120)
deck1(30, 40)
deck2(40, 30)
body(60,40,80,89.7)
triangle2(25,25)
turtle.exitonclick()






