import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width = 600, height = 600)
canvas.pack()
my_image = PhotoImage(file='/Users/julia/Documents/GitHub/python/dog.gif') 
canvas.create_image(0, 0, anchor=NW, image=my_image)
for x in range(0, 60):
	canvas.move(1,5,0)
	tk.update()
	time.sleep(0.005)

for x in range(0, 60): 
	canvas.move(1, 0, 5)
	tk.update() 
	time.sleep(0.005)

for x in range(0, 60):
	canvas.move(1,-5,0)
	tk.update()
	time.sleep(0.005)

for x in range(0, 60): 
	canvas.move(1, 0, -5)
	tk.update() 
	time.sleep(0.005)