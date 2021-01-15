#install gimp from https://www.gimp.org/ http:// gimp.lisanet.de/Website/Download.html.

# create transparent bbackground
#background Layer ▶ Transparency ▶ Add Alpha Channel 

#create graphics for the game

#human - a little man who can move to the right, left and jump; Stickman - a man drawn with lines

#platforms in three different sizes

#doors : open and close

#background (if we want the game to look nice, a solid white or gray background doesn't work for us). (something fun)

from tkinter import *
import random
import time
class Game:
	def __init__(self):
		self.tk = Tk()
	self.tk.title("man is seeking the exit") 
	self.tk.resizable(0, 0) 
	self.tk.wm_attributes("-topmost", 1)
	self.canvas = Canvas(self.tk, width=500, height=500, highlightthickness=0)
	self.canvas.pack() 
	self.tk.update() 
	self.canvas_height = 500 
	self.canvas_width = 500
	self.bg = PhotoImage(file="background.gif")
	w = self.bg.width()
	h = self.bg.height()
	for x in range(0, 5): 
		for y in range(0, 5):
		self.canvas.create_image(x * w, y * h,  image=self.bg, anchor='nw')
	self.sprites = [] 
	self.running = True

	def mainloop(self):
		while 1:
			if self.running == True:
				for sprite in self.sprites:
					sprite.move()
			self.tk.update_idletasks()
			self.tk.update()
			time.sleep(0.01)

g = Game() 
g.mainloop()

class Coords:
def __init__(self, x1=0, y1=0, x2=0, y2=0):
	self.x1 = x1 
	self.y1 = y1 
	self.x2 = x2 
	self.y2 = y2