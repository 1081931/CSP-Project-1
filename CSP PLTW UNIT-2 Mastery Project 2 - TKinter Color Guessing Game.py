import tkinter as tk
root = tk.Tk()
root.wm_geometry("400x600")


frame_color = tk.Frame(root)

canvas = tk.Canvas(root, width = 300, height = 200, background = "red")
canvas.pack()

canvas.config(ANCHOR=tk.CENTER)

canvas.create_text(50, 50, text = "hi", font = ("arial", 30))

red = tk.Button(root, text = "red", command  = "onclick", background = "red")
red.pack()

green = tk.Button(root, text = "green", command  = "onclick", background = "green")
green.pack()

blue = tk.Button(root, text = "blue", command  = "onclick", background = "blue")
blue.pack()

yellow = tk.Button(root, text = "yellow", command  = "onclick", background = "yellow")
yellow.pack()

orange = tk.Button(root, text = "orange", command  = "onclick", background = "orange")
orange.pack()

purple = tk.Button(root, text = "purple", command  = "onclick", background = "purple")
purple.pack()

pink = tk.Button(root, text = "pink", command  = "onclick", background = "pink")
pink.pack()

brown = tk.Button(root, text = "brown", command  = "onclick", background = "brown")
brown.pack()

black = tk.Button(root, text = "black", command  = "onclick", background = "black")
black.pack()

white = tk.Button(root, text = "white", command  = "onclick", background = "white")
white.pack()

root.mainloop()
