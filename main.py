import tkinter as tk
from tkinter import colorchooser

pen_color = "black"
pen_size = 2

def paint(event):
    x1, y1 = (event.x - pen_size), (event.y - pen_size)
    x2, y2 = (event.x + pen_size), (event.y + pen_size)
    canvas.create_oval(x1, y1, x2, y2, fill=pen_color, outline=pen_color)

def use_pen():
    global pen_color
    pen_color = "black"
    global pen_size
    pen_size = size_slider.get()

def use_brush():
    global pen_color
    pen_color = "black"
    global pen_size
    pen_size = size_slider.get() * 2

def choose_color():
    color = colorchooser.askcolor()
    if color:
        global pen_color
        pen_color = color[1]

def use_eraser():
    global pen_color
    pen_color = "white"
    global pen_size
    pen_size = size_slider.get() * 2

def change_size(val):
    global pen_size
    pen_size = int(val)

root = tk.Tk()
root.title("Simple Paint App")

canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

pen_button = tk.Button(root, text="Pen", command=use_pen)
pen_button.pack(side=tk.LEFT)

brush_button = tk.Button(root, text="Brush", command=use_brush)
brush_button.pack(side=tk.LEFT)

color_button = tk.Button(root, text="Color", command=choose_color)
color_button.pack(side=tk.LEFT)

eraser_button = tk.Button(root, text="Eraser", command=use_eraser)
eraser_button.pack(side=tk.LEFT)

size_slider = tk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL, label="Size", command=change_size)
size_slider.pack(side=tk.LEFT)

canvas.bind("<B1-Motion>", paint)

root.mainloop()
