from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_text(150, 100, text='once upon a time')
canvas.create_text(130, 120, text='in 2020.', fill='red')
mainloop()

canvas.create_text(150, 150, text='he said: oh gosh!,', font=('Times', 15))
canvas.create_text(200, 200, text='sometimes it can be worse',font=('Helvetica', 20)) 
canvas.create_text(220, 250, text='my bro is sitting there',font=('Courier', 22)) 
canvas.create_text(220, 300, text='on top of meduza".', font=('Courier',30))