import tkinter as tk
import math
import board
from tkinter import * 
root = Tk()
root.geometry('500x500')
root.resizable(False, False);
canvasHeight = 500
canvasWidth = 500
initialSeparation = canvasHeight/10
canvas = Canvas(root, height= canvasHeight, width= canvasWidth, bg="white")
fixOuterBarsFactor = 2
buttonWidth = 5
theBoard = board.Board()

def passInfo():
    for x in range(0, 9):
        for y in range(0, 9):
            theBoard.fillASquare(x, y, gridEntries[y][x].get())
    theBoard.printSets()
    
    return 

solveButton = Button(root, text = "Solve", command = passInfo, width = buttonWidth)
solveButton.place(x = (canvasWidth-buttonWidth)/2, y = 20, anchor = CENTER)
gridEntries = []

for y in range (10):
    rowEntry = []
    for x in range (10):
        rowEntry.append(StringVar())
        textBox = Entry(root, width=int(((canvasWidth-initialSeparation)/10)/36), bg = "white", relief='flat', textvariable = rowEntry[x])
        textBox.pack()
        textBox.place(x = ((canvasWidth-initialSeparation)/10.0)*(x+1) + 13, y = ((canvasWidth-initialSeparation)/10.0)*(y+1) + 10) 
    gridEntries.append(rowEntry)


    if (y % 3 == 0):
        if (y == 0 or y == 9): 
            line = canvas.create_line(((canvasWidth-initialSeparation)/10.0)*(y+1), (canvasWidth-initialSeparation)/10.0 - fixOuterBarsFactor, ((canvasWidth-initialSeparation)/10.0)*(y+1), canvasHeight - initialSeparation + fixOuterBarsFactor, width = 5)
            line = canvas.create_line((canvasWidth-initialSeparation)/10.0 - fixOuterBarsFactor, ((canvasWidth-initialSeparation)/10.0)*(y+1),  canvasHeight - initialSeparation + fixOuterBarsFactor, ((canvasWidth-initialSeparation)/10.0)*(y+1), width = 5)
        else:
            line = canvas.create_line(((canvasWidth-initialSeparation)/10.0)*(y+1), (canvasWidth-initialSeparation)/10.0, ((canvasWidth-initialSeparation)/10.0)*(y+1), canvasHeight - initialSeparation, width = 5)
            line = canvas.create_line((canvasWidth-initialSeparation)/10.0, ((canvasWidth-initialSeparation)/10.0)*(y+1),  canvasHeight - initialSeparation, ((canvasWidth-initialSeparation)/10.0)*(y+1), width = 5)
    else:
        line = canvas.create_line(((canvasWidth-initialSeparation)/10.0)*(y+1), (canvasWidth-initialSeparation)/10.0, ((canvasWidth-initialSeparation)/10.0)*(y+1), canvasHeight - initialSeparation, width = 3)
        line = canvas.create_line((canvasWidth-initialSeparation)/10.0, ((canvasWidth-initialSeparation)/10.0)*(y+1),  canvasHeight - initialSeparation, ((canvasWidth-initialSeparation)/10.0)*(y+1), width = 3)

canvas.pack()
mainloop()

