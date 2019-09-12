import turtle
turtle.shape("turtle")
fr = 300
turtle.speed(.3)

def rectangle():
        turtle.forward(fr)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(fr)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(180)
        turtle.forward(50)
        turtle.right(-90)


def russianflag():
    rectangle()
    turtle.color("blue")
    turtle.begin_fill()
    rectangle()
    turtle.end_fill()
    turtle.color("red")
    turtle.begin_fill()
    rectangle()
    turtle.end_fill()


def rectangle2():
    for i in range(2):
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)

def USrectangle():
    for i in range(3):
        turtle.begin_fill()
        turtle.penup()
        turtle.forward(300)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)
        turtle.forward(300)
        turtle.end_fill()
        turtle.right(-90)
        turtle.forward(20)
        turtle.right(-90)

def USrectangle2():
    for i in range(4):
        turtle.begin_fill()
        turtle.forward(450)
        turtle.right(-90)
        turtle.forward(20)
        turtle.right(-90)
        turtle.forward(450)
        turtle.end_fill()
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)
st = 15
def star():
    for i in range(5):
        turtle.forward(st)
        turtle.right(144)

def starrep():
    for i in range(10):
        turtle.begin_fill()
        star()
        turtle.end_fill()
        turtle.forward(st)

def USstar():
    for i in range(5):
        starrep()
        turtle.right(180)
        turtle.forward(150)
        turtle.right(-90)
        turtle.forward(18)
        turtle.right(-90)

def squr(size1, size2):
    for i in range(2):
        turtle.forward(size1)
        turtle.right(90)
        turtle.forward(size2)
        turtle.right(90)

def sqursp():
    for i in range(60):
        squr(i*2, i*4)









russianflag()
turtle.penup()
turtle.forward(-250)
turtle.right(-90)
turtle.forward(75)
turtle.right(-90)
turtle.forward(225)
turtle.color("blue")
#ppp
turtle.begin_fill()
rectangle2()
turtle.end_fill()
turtle.forward(150)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.pendown()
turtle.color("red")
turtle.forward(450)
turtle.right(90)
turtle.forward(240)
turtle.right(90)
turtle.forward(450)
turtle.right(90)
turtle.forward(240)
turtle.right(90)
turtle.forward(150)
USrectangle()
turtle.forward(300)
turtle.right(180)
USrectangle2()
turtle.forward(450)
turtle.right(90)
turtle.forward(270)
turtle.right(90)
turtle.color("white")
turtle.pendown()
USstar()
turtle.color("red")
turtle.speed(10)
turtle.penup()
turtle.right(-90)
turtle.forward(150)
turtle.right(90)
turtle.pendown()
turtle.forward(450)
turtle.right(-90)
turtle.forward(200)
turtle.right(-90)
turtle.forward(450)
turtle.right(-90)
turtle.forward(200)
turtle.right(-90)
turtle.penup()
turtle.speed(10)
turtle.right(-90)
turtle.forward(100)
turtle.right(90)
turtle.forward(170)
turtle.right(90)
turtle.begin_fill()
turtle.circle(60)
turtle.end_fill()
turtle.penup()
turtle.right(-90)
turtle.forward(400)
turtle.pendown()
turtle.right(-90)
turtle.forward(75)
turtle.right(90)
sqursp()






turtle.exitonclick()