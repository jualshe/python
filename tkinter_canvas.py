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

#to convert 15 from decimal to hexadecimal
>>>print('%x' % 15)
f
>>> print('%02x' % 15)
0f

from tkinter import * 
colorchooser.askcolor()

>>> colorchooser.askcolor()
((235.91796875, 86.3359375, 153.59765625), '#eb5699')

c = colorchooser.askcolor()
random_rectangle(400, 400, c[1])

#arc drawing
canvas.create_arc(10, 10, 200, 100, extent=180, style=ARC)


from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_arc(10, 10, 200, 100, extent=180, style=ARC)


canvas.create_arc(10, 10, 200, 80, extent=45, style=ARC)  
canvas.create_arc(10, 80, 200, 160, extent=90, style=ARC) 
canvas.create_arc(10, 160, 200, 240, extent=135, style=ARC)
canvas.create_arc(10, 240, 200, 320, extent=180, style=ARC)
canvas.create_arc(10, 320, 200, 400, extent=359, style=ARC)