from turtle import *
import turtle

def triangle(a, b):
    t.forward(a)
    t.left(135)
    t.forward(b)
    t.left(90)
    t.forward(b)
    t.left(135)


def parallelogram(a, b):
    for i in range(2):
        t.forward(a)
        t.left(45)
        t.forward(b)
        t.left(135)

def square(a):
    for i in range(4):
        t.forward(a)
        t.right(90)

t = turtle.Turtle()
w = turtle.Screen()

#ракета

#красный треугольник
t.color('red')
t.right(45)
t.forward(100)
t.left(135)
t.begin_fill()
triangle(141.5, 100)
t.end_fill()

#желтый треугольник
t.left(45)
t.forward(100)
t.right(45)
t.color('yellow')
t.forward(141.5)
t.left(180)
t.begin_fill()
triangle(141.5, 100)
t.end_fill()

#синий треугольник
t.left(45)
t.color('blue')
t.begin_fill()
triangle(100, 70.7)
t.end_fill()

#розовый треугольник
t.left(45)
t.color('pink')
t.begin_fill()
triangle(70.7, 50)
t.end_fill()

#оранжевый квадрат
t.right(90)
t.penup()
t.forward(141.5)
t.pendown()
t.left(45)
t.color('orange')
t.begin_fill()
square(50)
t.end_fill()

#фиолетовый треугольник
t.right(90)
t.forward(50)
t.left(45)
t.color('purple')
t.begin_fill()
triangle(70.7, 50)
t.end_fill()

#зеленый параллелограмм
t.left(135)
t.penup()
t.forward(150)
t.right(135)
t.forward(71.5)
t.pendown()
t.color('green')
t.begin_fill()
parallelogram(70, 60)
t.end_fill()

t.penup()
t.forward(500)

w.mainloop()