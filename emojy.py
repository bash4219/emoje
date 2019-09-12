import turtle


scn = turtle.Screen()
fas = turtle.Turtle()
ies = turtle.Turtle()
mawth = turtle.Turtle()

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



fase()
iese()



turtle.exitonclick()