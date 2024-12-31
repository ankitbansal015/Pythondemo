from turtle import*
import turtle

for i in range (15):
    pensize(4)
    pencolor("blueviolet")
    circle(50)
    forward(5)
    right(25)

def my_goto(x,y):
    turtle.pencolor("orange")
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

turtle.pendown()
my_goto(-150,150)
turtle.write('BY:-ankit_015',font=("Bradley Hand ITC",10,"bold"))
turtle.done