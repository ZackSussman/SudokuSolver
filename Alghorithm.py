import board

class Algorithm:
    
    theBoard = board.Board()

    def __init__(self, theBoard):
        self.theBoard = theBoard

    def solveBoard(self):
        
        #for each number, go through each row and see if there is only one box in the row that number can be 
        for num in range(1, 10):
            for row in range(0, 9):
                plausableBoxesForRow = []
                for box in range(0, 9):
                    if (self.theBoard.isLegalToPutNumInBox(num, box, row)):
                        plausableBoxesForRow.append(box)
                if (len(plausableBoxesForRow) == 1):
                    self.theBoard.fillASquare(plausableBoxesForRow[0], row, num)
                    print("Action!")

        #for each number, go through each collumn and see if there is only one box in the collumn that number can be 
        for num in range(1, 10):
            for collumn in range(0, 9):
                plausableBoxesForCollumn = []
                for box in range(0, 9):
                    if (self.theBoard.isLegalToPutNumInBox(num, collumn, box)):
                        plausableBoxesForCollumn.append(box)
                if (len(plausableBoxesForCollumn) == 1):
                    self.theBoard.fillASquare(collumn, plausableBoxesForCollumn[0], num)
                    print("action!")

        #for each number, go through each square and see if there is only one box in the square that number can be 
        for num in range(1, 10):
            for square in range(0, 9):
                plausableKeysForSquare = []
                for key in range(0, 9):
                    if (self.theBoard.isLegalToPutNumInBox(num, self.theBoard.convertSquareAndKeyToX(square, key), self.theBoard.convertSquareAndKeyToY(square, key))):
                        plausableKeysForSquare.append(key)
                if (len(plausableKeysForSquare) == 1):
                    self.theBoard.fillASquare(self.theBoard.convertSquareAndKeyToX(square, plausableKeysForSquare[0]), self.theBoard.convertSquareAndKeyToY(square, plausableKeysForSquare[0]), num) 
                    print("action!")


        self.theBoard.printSets()