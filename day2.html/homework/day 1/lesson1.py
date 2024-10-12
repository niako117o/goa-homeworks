from turtle import *

#we want to paint a house

#draw a square
speed(10)
width(5)
color("red")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#and of square

#making door
forward(70)
color("orange")
begin_fill()
left(90)
forward(120)
right(90)
forward(50)
right(90)
forward(120)
end_fill()
#and of door

#lets makea roof

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#and of roof

#lets make window
left(30)
forward(30)
left(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
#and of first window

#lets make second window
left(90)
forward(130)
left(90)
forward(200)
left(90)
forward(130)
left(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)




exitonclick()