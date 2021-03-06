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

def within_x(co1, co2):
	if (co1.x1 > co2.x1 and co1.x1 < co2.x2)\
		or (co1.x2 > co2.x1 and co1.x2 < co2.x2) \
		or (co2.x1 > co1.x1 and co2.x1 < co1.x2) \
		or (co2.x2 > co1.x1 and co2.x2 < co1.x2):
		return True
    else:
    	return False

def within_y(co1, co2):
	if (co1.y1 > co2.y1 and co1.y1 < co2.y2) \
		or (co1.y2 > co2.y1 and co1.y2 < co2.y2) \
		or (co2.y1 > co1.y1 and co2.y1 < co1.y2) \
		or (co2.y2 > co1.y1 and co2.y2 < co1.y2):
              return True
          else:
return False

def collided_left(co1, co2):
	if within_y(co1, co2):
		if co1.x1 <= co2.x2 and co1.x1 >= co2.x1:
			return True
	return False

#c1 = Coords(40, 40, 100, 100)
#c2 = Coords(50, 50, 150, 150)
#print(within_x(c1, c2))
#True

def within_x(co1, co2):
	if (co1.x1 > co2.x1 and co1.x1 < co2.x2) \
		or (co1.x2 > co2.x1 and co1.x2 < co2.x2) \
		or (co2.x1 > co1.x1 and co2.x1 < co1.x2) \
		or (co2.x2 > co1.x1 and co2.x2 < co1.x2):
              return True
          else:
return False

def collided_left(co1, co2):
	if within_y(co1, co2):
		if co1.x1 <= co2.x2 and co1.x1 >= co2.x1:
			return True
	return False

def collided_right(co1, co2):
	if within_y(co1, co2):
   		if co1.x2 >= co2.x1 and co1.x2 <= co2.x2: 
   			return True
	return False

def collided_top(co1, co2):
	if within_x(co1, co2):
		if co1.y1 <= co2.y2 and co1.y1 >= co2.y1:
			return True
	return False

def collided_bottom(y, co1, co2):
    if within_x(co1, co2):
    	y_calc = co1.y2 + y
    	if y_calc >= co2.y1 and y_calc <= co2.y2:
            return True
    return False

class Sprite:
    def __init__(self, game):
    	self.game = game 
    	self.endgame = False 
    	self.coordinates = None
    def move(self):
        pass
	def coords(self):
		return 
		self.coordinates
 