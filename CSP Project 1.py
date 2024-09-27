# Project
import turtle as trtl
x = trtl.Turtle()

color_list = ["red","blue","yellow","purple","green"]

x.speed(100)
x.pensize(5)
radius = int(input("Enter the radius of the circle"))
step = int(input("Enter the amount of steps that you want"))
repeat = 1
color = 1
step_angle = int(input("What do you want the angle between each shape to be?"))


while repeat == 1:
  x.pencolor("black")
  x.fillcolor(color_list[color%len(color_list)])
  x.begin_fill()
  x.circle(radius,360,step)
  x.end_fill()
  x.left(step_angle)
  color+=1
  
wn = trtl.Screen()
wn.mainloop()

