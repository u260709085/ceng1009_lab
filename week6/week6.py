# import turtle
# tess = turtle.Turtle()
# tess.color("pink")
# screen = turtle.Screen()
# tess.pensize(5)
# screen.bgcolor("lightgreen")
# def drawPoly(tess,somesides,somesize):
#     for i in range(somesize):
#         tess.forward(100)
#         tess.left(45)
# drawPoly(tess,8,50)
#
#
#
#
#
# screen.exitonclick()
# import turtle
# tess = turtle.Turtle()
# screen = turtle.Screen()
# screen.bgcolor("lightgreen")
# tess.color("blue")
# tess.pensize(1)
# def drawpoly(someturtle,someside,somesize):
#     angle=360/someside
#     for i in range(someside):
#         someturtle.forward(somesize)
#         someturtle.left(angle)
# Exercise 2
# for i in range(20):
#     drawpoly(tess,4,100)
#     tess.left(18)
# def drawSpiral(someturtle,angle):
#     size = 1
#     for i in range(100):
#         someturtle.forward(size)
#         someturtle.right(angle)
#         size = size + 2
# def drawEquitriangle(someturtle,somesize):
#     drawpoly(someturtle,3,somesize)
# def drawStar(someturtle,size):
#     for i in range(5):
#         someturtle.forward(size)
#         someturtle.right(144)
# def drawSprite(someturtle,legs, lenght):
#     angle = 360/legs
#     for i in range(legs):
#         someturtle.forward(lenght)
#         someturtle.backward(lenght)
#         someturtle.left(angle)
# Exercise 3
# tess.pencolor("blue")
# tess.penup()
# tess.goto(-150,10)
# tess.pendown()
# drawSpiral(tess,90)
#
# tess.penup()
# tess.goto(150,0)
# tess.pendown()
# drawSpiral(tess,89)
# Exercise 4
# drawEquitriangle(tess,100)

# Exercise 5
# tess.pencolor("hotpink")
# for i in range(5):
#     drawStar(tess,50)
#     tess.penup()
#     tess.forward(200)
#     tess.right(144)
#     tess.pendown()
# Exercise 6
# drawSprite(tess,15,120)
#
#
#
# screen.exitonclick()
