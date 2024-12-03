import tkinter as tk
root = tk.Tk()
root.wm_geometry("400x600")


frame_color = tk.Frame(root)

red = tk.Button(root, text = "red", command  = "onclick")
red.grid(row = 0, column = 0)

green = tk.Button(root, text = "green", command  = "onclick")
green.grid(row = 0, column = 1)

blue = tk.Button(root, text = "blue", command  = "onclick")
blue.grid(row = 0, column = 2)

yellow = tk.Button(root, text = "yellow", command  = "onclick")
yellow.grid(row = 0, column = 3)

orange = tk.Button(root, text = "orange", command  = "onclick")
orange.grid(row = 0, column = 4)

purple = tk.Button(root, text = "purple", command  = "onclick")
purple.grid(row = 0, column = 5)

pink = tk.Button(root, text = "pink", command  = "onclick")
pink.grid(row = 0, column = 6)

brown = tk.Button(root, text = "brown", command  = "onclick")
brown.grid(row = 0, column = 7)

black = tk.Button(root, text = "black", command  = "onclick")
black.grid(row = 0, column = 8)

white = tk.Button(root, text = "white", command  = "onclick")
white.grid(row = 0, column = 9)

root.mainloop()
