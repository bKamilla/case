import turtle

def sqareTurtle(root, step, angle, colorPen=None, colorFill=None, rotate="left"):
    if colorPen != None:
        root.pencolor(colorPen)

    if colorFill != None:
        root.color(colorPen, colorFill)

    root.begin_fill()
    for _ in range(0, 4):
        root.forward(step)
        if rotate == "left":
            root.left(angle)
        else:
            root.right(angle)
    root.end_fill()
    root.pencolor(colorPen)

def main(root):
    root.shape("turtle")
    root.speed(3)
    root.pensize(3)

    root.penup()
    root.goto(-200, 200)
    root.pendown()

#треугольник
    root.color('purple', 'purple')
    root.begin_fill()
    root.forward(70)
    root.left(135)
    root.forward(50)
    root.end_fill()

    root.left(135)
    root.penup()
    root.goto(-198, 190)
    root.pendown()
# треугольник
    root.color('blue', 'blue')
    root.begin_fill()
    root.forward(120)
    root.left(135)
    root.forward(95)
    root.end_fill()

    root.penup()
    root.goto(-131, 143)
    root.pendown()
#треугольник
    root.color('orange', 'orange')
    root.begin_fill()
    root.left(45)
    root.forward(50)
    root.left(90)
    root.forward(65)
    root.end_fill()

    root.left(90)
    root.penup()
    root.forward(131)
    root.left(90)
    root.forward(65)
    root.left(90)
    root.forward(68)
    root.pendown()
# треугольник
    root.color('red', 'red')
    root.begin_fill()
    root.left(180)
    root.forward(125)
    root.right(135)
    root.forward(87)
    root.end_fill()

    root.left(135)
    root.penup()
    root.forward(5)
    root.right(90)
    root.forward(5)
    root.left(135)
    root.pendown()
#квадрат
    sqareTurtle(root, 45, 90, "green", "green", "right")

    root.right(45)
    root.penup()
    root.forward(70)
    root.right(90)
    root.forward(4)
    root.right(45)
    root.pendown()
# треугольник
    root.color('pink', 'pink')
    root.begin_fill()
    root.forward(46)
    root.left(135)
    root.forward(67)
    root.end_fill()

    root.left(90)
    root.penup()
    root.forward(110)
    root.left(90)
    root.forward(34)
    root.pendown()
#пареллелограмм
    root.color("purple", "purple")
    root.begin_fill()
    for _ in range(0, 2):
        root.forward(62)
        root.right(135)
        root.forward(45)
        root.right(45)
    root.end_fill()

    turtle.exitonclick()

if __name__ == "__main__":
    root = turtle.Turtle()
    main(root)