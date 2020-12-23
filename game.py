from tkinter import *
import random
import time

#Delay before the start of the game - time.sleep(2)

import tkinter as tk
root = tk.Tk()
var = tk.IntVar()
button = tk.Button(root, text="Start Game!!!", command=lambda: var.set(1))
button.place(relx=.5, rely=.5, anchor="c")
button.wait_variable(var)

class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10,10,25,25, fill=color)
        self.canvas.move(self.id, 245,100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
            return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        
    def turn_left(self, evt):
        self.x = -2
    def turn_right(self, evt):
        self.x = 2
        
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

paddle = Paddle(canvas, 'blue')
ball = Ball(canvas,paddle, 'red')

while 1:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    tk.update_idletasks() 
    tk.update() 
    time.sleep(0.01)

root.after(2000, game_over)

def game_over():
	tk = Tk()
	canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
	canvas.pack()
	canvas.create_text(150, 100, text='game over!!')
	canvas.create_text(130, 120, text='in 2020.', fill='red')
	tk.update()

#Game score - add a game score showing how many times user played and won

#Ball acceleration - increase the speed of the ball

#End Game Screen - show game is over screen
#create_ text
#itemconfig (normal and hidden)

#print(self.canvas.coords(self.id))
#[255.0, 29.0, 270.0, 44.0]