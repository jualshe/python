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