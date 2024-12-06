import tkinter as tk
import random

root = tk.Tk()
root.wm_geometry("400x600")

colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", "black", "white"]
variable = random.choice(colors)
remaining_time = 60
score = 0
game_active = True  

def button(color):
    global variable, score, game_active
    if game_active:  
        if color == variable:
            score += 1
            score_label.config(text=f"Score: {score}")
        variable = random.choice(colors)
        canvas.config(background=variable)

def countdown(time_left):
    global remaining_time, game_active
    remaining_time = time_left  
    if remaining_time >= 0:
        timer_label.config(text=f"Time left: {remaining_time} seconds")
        root.after(1000, countdown, remaining_time - 1)
    else:
        timer_label.config(text="Time's up!")
        game_active = False  

def center_text():
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    canvas.create_text(canvas_width / 2, canvas_height / 2, text="Guess the Color!", font=("Arial", 15), anchor="center")

canvas = tk.Canvas(root, width=300, height=200, background=variable)
canvas.pack(fill="x", padx=50, pady=2)

root.after(100, center_text)

timer_label = tk.Label(root, text=f"Time left: {remaining_time} seconds")
timer_label.pack()

score_label = tk.Label(root, text=f"Score: {score}")
score_label.pack()

countdown(remaining_time)

for color in colors:
    btn = tk.Button(root, text=color, background=color, command=lambda c=color: button(c))
    btn.pack(fill="x", padx=50, pady=2)

root.mainloop()
