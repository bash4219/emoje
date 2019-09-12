import turtle


scn = turtle.Screen()
fas = turtle.Turtle()
ies = turtle.Turtle()
mawth = turtle.Turtle()
ieeball = turtle.Turtle()
mawth.speed(.5)

def fase():
    fas.color("Yellow")
    fas.begin_fill()
    fas.circle(150)
    fas.end_fill()

def iese():
    ies.penup()
    ies.right(-90)
    ies.forward(190)
    ies.right(-90)
    ies.forward(40)
    ies.right(90)
    ies.color("Black")
    ies.begin_fill()
    ies.circle(20)
    ies.end_fill()
    ies.right(90)
    ies.forward(80)
    ies.right(90)
    ies.begin_fill()
    ies.circle(20)
    ies.end_fill()
    ies.goto(0, 0,)

def mowth():
    mawth.penup()
    mawth.right(-90)
    mawth.forward(110)
    mawth.pendown()
    mawth.right(-90)
    mawth.forward(90)
    mawth.right(180)
    mawth.forward(180)
    mawth.right(90)
    mawth.begin_fill()
    for i in range(360):
        mawth.right(.5)
        mawth.forward(.8)
    mawth.right(90)
    mawth.forward(180)
    mawth.end_fill()



fase()
iese()
mowth()

turtle.exitonclick()