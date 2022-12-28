import turtle

laki=turtle.Turtle()
laki.shape('turtle')
laki.color('green')
laki.width(3)
laki.penup()
laki.goto(-10,-10)
laki.pendown()

for i in range(16):
    for j in range(10):
        laki.forward(100)
        laki.left(45)
    laki.left(45)