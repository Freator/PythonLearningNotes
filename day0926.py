# -*- coding:utf-8 -*-
import turtle
turtle.setup(680,280,200,200)
turtle.pensize(5)
turtle.speed(3)
turtle.color("red")
turtle.up()
def polygon(x,y,keep,fd,angle):
	turtle.goto(x,y)
	turtle.down()
	for i in range(keep):
		turtle.forward(fd)
		turtle.right(angle)
	turtle.up()
polygon(-300,100,4,180,360/4) #square
polygon(-80,100,3,200,360/3) #triangle
polygon(160,100,10,50,360/10)#hexagon
if input() == '\n':
	print("END")