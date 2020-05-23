import board


class Algorithm:
    
    theBoard = board.Board()
    solvedSquares = 0
    def __init__(self, theBoard):
        self.theBoard = theBoard
        self.solvedSquares = 0

    def solveBoard(self):
        solved = False
        pastNumberOfUnsolvedSquares = 81
        while solved == False:

            #for each number, go through each row and see if there is only one box in the row that number can be 
            for num in range(1, 10):
                for row in range(0, 9):
                    plausableBoxesForRow = []
                    for box in range(0, 9):
                        if (self.theBoard.isLegalToPutNumInBox(num, box, row)):
                            #print(str(num) + "is valid for (" + str(box) + ", " + str(row) + ")" + "row of: " + str(row) )
                            plausableBoxesForRow.append(box)
                    if (len(plausableBoxesForRow) == 1):
                        #print("for row " + str(row) + ", we will add " + str(num) + " to (" + str(plausableBoxesForRow[0]) + ", " + str(row) )
                        self.theBoard.fillASquare(plausableBoxesForRow[0], row, num)
                        self.solvedSquares = self.solvedSquares + 1

                    

            #for each number, go through each collumn and see if there is only one box in the collumn that number can be 
            for num in range(1, 10):
                for collumn in range(0, 9):
                    plausableBoxesForCollumn = []
                    for box in range(0, 9):
                        if (self.theBoard.isLegalToPutNumInBox(num, collumn, box)):
                            plausableBoxesForCollumn.append(box)
                            #print(str(num) + "is valid for (" + str(collumn) + ", " + str(box) + ")" )
                    if (len(plausableBoxesForCollumn) == 1):
                        self.theBoard.fillASquare(collumn, plausableBoxesForCollumn[0], num)
                        self.solvedSquares = self.solvedSquares + 1
                        

            #for each number, go through each square and see if there is only one box in the square that number can be 
            for num in range(1, 10):
                for square in range(0, 9):
                    plausableKeysForSquare = []
                    for key in range(0, 9):
                        #print(self.theBoard.isLegalToPutNumInBox(num, self.theBoard.convertSquareAndKeyToX(square, key), self.theBoard.convertSquareAndKeyToY(square, key)))
                        if (self.theBoard.isLegalToPutNumInBox(num, self.theBoard.convertSquareAndKeyToX(square, key), self.theBoard.convertSquareAndKeyToY(square, key))):
                            plausableKeysForSquare.append(key)
                            #print(str(num) + "is valid for (" + str(self.theBoard.convertSquareAndKeyToX(square, key)) + ", " + str(self.theBoard.convertSquareAndKeyToY(square, key)) + ")"  )
                    if (len(plausableKeysForSquare) == 1):
                        self.theBoard.fillASquare(self.theBoard.convertSquareAndKeyToX(square, plausableKeysForSquare[0]), self.theBoard.convertSquareAndKeyToY(square, plausableKeysForSquare[0]), num) 
                        self.solvedSquares = self.solvedSquares + 1
            
            unsolvedSquares = self.theBoard.getNumberOfUnsolvedSquares()
            if unsolvedSquares == pastNumberOfUnsolvedSquares:
                break
            else:
                pastNumberOfUnsolvedSquares = unsolvedSquares
            
            if (pastNumberOfUnsolvedSquares == 0):
                solved = True
        
        if solved == False:
            print("failed to solve board. Was able to solve " + str(self.solvedSquares))
            self.theBoard.printSets()
        else:
            print("success!")
        
        return solved


        
    