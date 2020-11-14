from tkinter import *
tk = Tk()
btn = Button(tk, text="press me") 
btn.pack()


# import turtle
# t = turtle.Pen()
#or
# from turtle import * 
# t = Pen()


 def hello():
 	print('helloooo')


from tkinter import *
tk = Tk()
btn = Button(tk, text="press me", command=hello)
btn.pack()


from tkinter import * ttk
ttk.Button(text="Login").pack()


import tkinter
tkinter.Button(None, text='button').pack()
tkinter.mainloop()

#latest working version
from tkinter import *
tk = Tk()
btn = Button(tk, text="press me") 
btn.mainloop()
