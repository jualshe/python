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