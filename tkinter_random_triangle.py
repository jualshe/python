from tkinter import *
import random
tk = Tk()
canvas = Canvas(tk, width=400, height=400) 
canvas.pack()
def random_triangle(width, height, fill_color):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = random.randrange(x1 + random.randrange(width))
    y2 = random.randrange(y1 + random.randrange(height))
    x3 = random.randrange(x2 + random.randrange(width))
    y3 = random.randrange(y2 + random.randrange(height))
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill=fill_color)

#run module
random_triangle(400, 400, '#ffd800')
random_triangle(400, 400, 'green')



for x in range(0, 5):
	random_triangle(400, 400, 'cyan')