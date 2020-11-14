from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
mainloop()

#drawing lines
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=500, height=500) 
canvas.pack()
canvas.create_line(0, 0, 500, 500)
1
mainloop()

import turtle
turtle.setup(width=500, height=500) 
t = turtle.Pen()
t.up()
t.goto(-250, 250)
t.down()
t.goto(500, -500)

#square
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_rectangle(10, 10, 50, 50)
mainloop()

from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_rectangle(10, 10, 300, 50)
