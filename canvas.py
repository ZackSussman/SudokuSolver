import tkinter as tk
import math
from tkinter import * 
root = Tk()
root.geometry('500x500')
root.resizable(False, False);
canvasHeight = 500
canvasWidth = 500
initialSeparation = canvasHeight/10
canvas = Canvas(root, height= canvasHeight, width= canvasWidth, bg="white")
fixOuterBarsFactor = 2

def passInfo():
    return 

solveButton = Button(text = "Solve", command = passInfo )
gridEntries = []

for x in range (10):
    rowEntry = []
    for y in range (10):
        rowEntry.append(StringVar())
        textBox = Entry(root, width=int(((canvasWidth-initialSeparation)/10)/36), bg = "white", relief='flat', textvariable = rowEntry[y])
        textBox.pack()
        textBox.place(x = ((canvasWidth-initialSeparation)/10.0)*(x+1) + 13, y = ((canvasWidth-initialSeparation)/10.0)*(y+1) + 10 ) 
    gridEntries.append(rowEntry)


    if (x % 3 == 0):
        if (x == 0 or x == 9): 
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


for row in gridEntries: 
    for entry in row:
        print(entry.get())
    print("\n")