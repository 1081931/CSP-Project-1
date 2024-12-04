import tkinter as tk
import random
from turtle import onclick
root = tk.Tk()
root.wm_geometry("400x600")


frame_color = tk.Frame(root)


colors = ["red","green","blue","yellow","orange", "purple", "pink", "brown", "black", "white"]
variable = random.choice(colors)

def button(color):
    if color == variable:
        print("congrats")
    else:
        print("u are dumdum")

canvas = tk.Canvas(root, width = 300, height = 200, background = variable)
canvas.pack()

canvas.create_text(50, 50, text = "hi", font = ("arial", 30))

red = tk.Button(root, text = "red", background = "red", command = lambda: button("red"))
red.pack()

green = tk.Button(root, text = "green", background = "green", command = lambda: button("green"))
green.pack()

blue = tk.Button(root, text = "blue", background = "blue", command = lambda: button("blue"))
blue.pack()

yellow = tk.Button(root, text = "yellow", background = "yellow", command = lambda: button("yellow"))
yellow.pack()

orange = tk.Button(root, text = "orange", background = "orange", command = lambda: button("orange"))
orange.pack()

purple = tk.Button(root, text = "purple", background = "purple", command = lambda: button("purple"))
purple.pack()

pink = tk.Button(root, text = "pink", background = "pink", command = lambda: button("pink"))
pink.pack()

brown = tk.Button(root, text = "brown", background = "brown", command = lambda: button("brown"))
brown.pack()

black = tk.Button(root, text = "black", background = "black", command = lambda: button("black"))
black.pack()

white = tk.Button(root, text = "white", background = "white", command = lambda: button("white"))
white.pack()


root.mainloop()
