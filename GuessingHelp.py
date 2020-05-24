import board

class GuessingHelp():
    original = None
    possibleValuesForSquare = None
    def __init__(self, initialState):
        self.original = initialState


    def makeGuess(self, changeGuess):
        newBoard = board.Board(self.original.sets)
        xFill = 0
        yFill = 0
        found = False
        for y in range(0, 9):
            for x in range(0, 9):
                if len(newBoard.getPossibleValuesForSquare(x, y)) == 2:
                    self.possibleValuesForSquare = newBoard.getPossibleValuesForSquare(x, y)
                    print(str(self.possibleValuesForSquare) + str(changeGuess))
                    found = True
                    xFill = x
                    yFill = y
                    break
            if found == True:
                break
        if (changeGuess):
            print(str(self.possibleValuesForSquare) + str(changeGuess))
            newBoard.fillASquare(xFill, yFill, self.possibleValuesForSquare[1])
            return newBoard
        
        else:
            newBoard.fillASquare(xFill, yFill, self.possibleValuesForSquare[0])
            return newBoard


 