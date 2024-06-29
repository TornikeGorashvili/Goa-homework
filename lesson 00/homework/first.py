from turtle import *

# print("toko")
# print (5)
# print ("5")

# print (5 + int("5"))
# print ("toko aris " + "5" + " wlis" )



#we want to paint a house

#step one: draw a square
shape("turtle")
speed(50)
width(10)
color("green")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(66)
left(90)

color("purple")
begin_fill()
forward(100)
right(90)

forward(66)
right(90)

forward(100)
right(90)

forward(66)
end_fill()

color("red")
begin_fill()
penup()
goto(200, 200)
pendown()

color("green")
right(50)
forward(150)

left(98)
forward(150)

left(132)
forward(199)

end_fill()

penup()
goto(0,0)
pendown()

begin_fill()
left(90)
forward(100)
color("blue")
right(90)
forward(66)
left(90)
forward(50)
left(90)
forward(66)
left(90)
forward(50)
end_fill()

penup()
goto(200,0)
pendown()

color("green")
begin_fill()
left(180)
forward(100)
color("blue")
left(90)
forward(66)
right(90)
forward(50)
right(90)
forward(66)
right(90)
forward(50)
end_fill()




exitonclick()