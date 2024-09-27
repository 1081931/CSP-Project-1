# Project
import turtle as trtl
x = trtl.Turtle()

color_list = ["red","blue","yellow","purple","green"]


pensize = int(input("Enter a pen size"))
x.pensize(pensize)
radius = int(input("Enter the radius of the circle"))
step = int(input("Enter the amount of steps that you want"))
repeat = int(input("How many times do you want the pattern to repeat"))
step_angle = int(input("What do you wnat the angle between each shape to be?"))

for i in range(repeat):
  x.pencolor("black")
  x.fillcolor(color_list[i%len(color_list)])
  x.begin_fill()
  x.circle(radius,360,step)
  x.end_fill()
  x.left(step_angle)
  
wn = trtl.Screen()
wn.mainloop()
#idk
