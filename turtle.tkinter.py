from tkinter import *
tk = Tk()
btn = Button(tk, text="press me") 
btn.pack()


# import turtle
# t = turtle.Pen()
#or
# from turtle import * 
# t = Pen()

#latest working version
from tkinter import *
tk = Tk()
btn = Button(tk, text="press me")
btn.pack()
btn = Button(tk, text="press me")
btn.pack()
mainloop()

def hello():
	print('helloooo')


from tkinter import *
tk = Tk()
btn = Button(tk, text="press me", command=hello)
btn.pack()
mainloop()

def person(width, height):
	print('My width - %s, and my height - %s' % (width, height))
 
person(4, 3)
person(height=3, width=4)