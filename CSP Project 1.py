# Project
import turtle as trtl
x = trtl.Turtle()
x.pensize(30)
i=int(input("Enter the length of the star"))
z=int(input("Enter the angle"))
for i in range(4):
  x.forward(i)
  x.right(120)
wn = trtl.Screen()
wn.mainloop()
#idk
