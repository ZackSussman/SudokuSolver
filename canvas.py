import tkinter as tk
import math
from tkinter import * 
root = Tk()
root.geometry('500x500')


canvasHeight = 500
canvasWidth = 500
initialSeparation = canvasHeight/10
canvas = Canvas(root, height= canvasHeight, width= canvasWidth, bg="white")
fixOuterBarsFactor = 2


for x in range (10):
    for y in range (10):
        textBox = Entry(root, width=int(((canvasWidth-initialSeparation)/10)/36), bg = "white", relief='flat')
        textBox.pack()
        textBox.place(x = ((canvasWidth-initialSeparation)/10.0)*(x+1) + 13, y = ((canvasWidth-initialSeparation)/10.0)*(y+1) + 10 )

    if (x % 3 == 0):
        if (x == 0 or x == 9): 
            zack = 2
            line = canvas.create_line(((canvasWidth-initialSeparation)/10.0)*(x+1), (canvasWidth-initialSeparation)/10.0 - fixOuterBarsFactor, ((canvasWidth-initialSeparation)/10.0)*(x+1), canvasHeight - initialSeparation + fixOuterBarsFactor, width = 5)
            line = canvas.create_line((canvasWidth-initialSeparation)/10.0 - fixOuterBarsFactor, ((canvasWidth-initialSeparation)/10.0)*(x+1),  canvasHeight - initialSeparation + fixOuterBarsFactor, ((canvasWidth-initialSeparation)/10.0)*(x+1), width = 5)
        else:
            line = canvas.create_line(((canvasWidth-initialSeparation)/10.0)*(x+1), (canvasWidth-initialSeparation)/10.0, ((canvasWidth-initialSeparation)/10.0)*(x+1), canvasHeight - initialSeparation, width = 5)
            line = canvas.create_line((canvasWidth-initialSeparation)/10.0, ((canvasWidth-initialSeparation)/10.0)*(x+1),  canvasHeight - initialSeparation, ((canvasWidth-initialSeparation)/10.0)*(x+1), width = 5)
    else:
        line = canvas.create_line(((canvasWidth-initialSeparation)/10.0)*(x+1), (canvasWidth-initialSeparation)/10.0, ((canvasWidth-initialSeparation)/10.0)*(x+1), canvasHeight - initialSeparation, width = 3)
        line = canvas.create_line((canvasWidth-initialSeparation)/10.0, ((canvasWidth-initialSeparation)/10.0)*(x+1),  canvasHeight - initialSeparation, ((canvasWidth-initialSeparation)/10.0)*(x+1), width = 3)

canvas.pack()
mainloop()