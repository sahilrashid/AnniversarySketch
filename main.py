import os.path
import time
import turtle
from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor('light pink')

screen.addshape(os.path.expanduser('C:/Users\sahil/Downloads/pic1.gif'))
turtle.shape(os.path.expanduser('C:/Users\sahil/Downloads/pic1.gif'))

screen.setup(width=1920, height=1080, startx=0, starty=0)

time.sleep(2)

turtle = Turtle()
turtle.hideturtle()
turtle.color('white')
turtle.begin_fill()
turtle.fillcolor('white')
turtle.left(140)
turtle.forward(180)
turtle.circle(-90, 200)
turtle.setheading(60)
turtle.circle(-90, 200)
turtle.forward(180)
turtle.end_fill()


turtle.sety(-100)
turtle.color('white')
style = ('Courier', 50, 'italic')
turtle.write('Happy Anniversary Maham <3', font=style, align='center')



screen.mainloop()