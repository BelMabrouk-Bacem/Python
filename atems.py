import turtle

from turtle import *

import colorsys

a=turtle.Turtle()
an=turtle.Screen()
a.turtlesize(5)

turtle.bgcolor("black") 
a.speed(1)
h=0
c=colorsys.hsv_to_rgb(h,1,1)

a.color("red") #cyan
a.pensize(20)
a.penup()
a.left(150)
a.fd(300) 
a.left(95)

# write A letter
a.pendown()
a.fd(140)
a.bk(140)
a.left(115) 
a.right(60)
a.fd(140) 
a.bk(60)
a.right(120)
a.fd(70)

#giving space 
a.penup()
a.bk(180)
a.right(90)
a.bk(50)
a.pendown() 

a.color("blue")
# write T letter
a.fd(120)
a.right(90) 
a.fd(60)
a.bk(120)

#giving space 
a.penup()
a.bk(-180)
a.right(-90)
a.bk(60)
a.pendown() 

# Write E letter
a.bk(60)
a.fd(120)
a.right(90) 
a.fd(80)
a.bk(80) 
a.left(90)
a.bk(60)
a.right(90) 
a.fd(70)
a.bk(70)
a.left(90)
a.bk(60)
a.right(90) 
a.fd(90)

#giving space 
a.penup()
a.bk(-70)
a.left(90)
a.fd(60)
a.pendown() 

# write M letter
a.bk(60)
a.fd(120)
a.right(135) 
a.fd(70)
a.left(90)
a.fd(70)
a.right(135)
a.fd(120)

#giving space 
a.penup()
a.left(90)
a.bk(-130)
a.right(90)
a.bk(120)
a.right(90)
a.pendown() 

# write S letter
a.pendown() 
a.fd(60)
a.left(90)
a.fd(60)
a.left(90) 
a.fd(60)
a.right(90)
a.fd(60)
a.right(90)
a.fd(60) 

#giving space 
a.penup()
a.left(90)
a.bk(170)
a.left(90)
a.bk(125)
a.right(90)
a.pendown() 

#make star
a.color("red") 
a.pensize(5)
for i in range(5):
    a.fd(50)
    a.left(145)
   
#giving space 
a.penup()
a.left(90)
a.bk(480)
a.left(90)
a.fd(20)
a.left(90)
a.pendown() 

#make semicirle
a.pensize(15)
a.circle(100,220)

#end
a.penup()
a.bk(180)
a.right(360)
hideturtle