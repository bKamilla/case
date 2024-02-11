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

    root.color("green", "green")
    root.begin_fill()
    for _ in range(0, 2):
        root.left(135)
        root.forward(100)
        root.left(45)
        root.forward(70)
    root.end_fill()

    root.penup()
    root.goto(-235, 195)
    root.pendown()
#квадрат
    sqareTurtle(root, 70, 90, "orange", "orange", "right")

    root.penup()
    root.goto(-235, 195)
    root.pendown()
#параллелограмм
    root.color("black", "black")
    root.begin_fill()
    for _ in range(0, 2):
        root.left(135)
        root.forward(100)
        root.left(45)
        root.forward(70)
    root.end_fill()

    root.penup()
    root.goto(-240, 160)
    root.pendown()
#треугольник
    root.color("red", "red")
    root.begin_fill()
    root.right(90)
    root.forward(130)
    root.right(90)
    root.forward(130)
    root.end_fill()

    root.penup()
    root.goto(-370, 25)
    root.pendown()
#треугольник
    root.color("yellow", "yellow")
    root.begin_fill()
    root.left(90)
    root.forward(130)
    root.left(135)
    root.forward(185)
    root.end_fill()

    root.left(45)
    root.penup()
    root.goto(-235, -10)
    root.pendown()

#треугольник
    root.color('purple', 'purple')
    root.begin_fill()
    root.forward(70)
    root.right(135)
    root.forward(50)
    root.end_fill()

    root.left(45)
    root.penup()
    root.goto(-370, -110)
    root.pendown()
#треугольник
    root.color("blue", "blue")
    root.begin_fill()
    root.forward(90)
    root.left(90)
    root.forward(90)
    root.end_fill()

    root.left(45)
    root.penup()
    root.goto(-275, -50)
    root.pendown()
#треугольник
    root.color("pink", "pink")
    root.begin_fill()
    root.left(135)
    root.forward(60)
    root.left(90)
    root.forward(60)
    root.end_fill()

    turtle.exitonclick()

if __name__ == "__main__":
    root = turtle.Turtle()
    main(root)