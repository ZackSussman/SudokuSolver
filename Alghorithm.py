import board
import TestingSets


class Algorithm:
    theBoard = board.Board(TestingSets.emptyBoard)
    solvedSquares = 0
    guessingBoards = []
    def __init__(self, theBoard):
        self.theBoard = theBoard
        self.guessingBoards.append(board.Board(theBoard.sets))
        self.solvedSquares = 0


    def checkEachGroupIfOnlyOneSpotFitsForEachNumber(self, solvingBoardNumber):
            #for each number, go through each row and see if there is only one box in the row that number can be 
            for num in range(1, 10):
                for row in range(0, 9):
                    plausableBoxesForRow = []
                    for box in range(0, 9):
                        if (self.guessingBoards[solvingBoardNumber].isLegalToPutNumInBox(num, box, row)):
                            #print(str(num) + "is valid for (" + str(box) + ", " + str(row) + ")" + "row of: " + str(row) )
                            plausableBoxesForRow.append(box)
                    if (len(plausableBoxesForRow) == 1):
                        #print("for row " + str(row) + ", we will add " + str(num) + " to (" + str(plausableBoxesForRow[0]) + ", " + str(row) )
                        self.guessingBoards[solvingBoardNumber].fillASquare(plausableBoxesForRow[0], row, num)
                        self.solvedSquares = self.solvedSquares + 1

                    

            #for each number, go through each collumn and see if there is only one box in the collumn that number can be 
            for num in range(1, 10):
                for collumn in range(0, 9):
                    plausableBoxesForCollumn = []
                    for box in range(0, 9):
                        if (self.guessingBoards[solvingBoardNumber].isLegalToPutNumInBox(num, collumn, box)):
                            plausableBoxesForCollumn.append(box)
                            #print(str(num) + "is valid for (" + str(collumn) + ", " + str(box) + ")" )
                    if (len(plausableBoxesForCollumn) == 1):
                        self.guessingBoards[solvingBoardNumber].fillASquare(collumn, plausableBoxesForCollumn[0], num)
                        self.solvedSquares = self.solvedSquares + 1
                        

            #for each number, go through each square and see if there is only one box in the square that number can be 
            for num in range(1, 10):
                for square in range(0, 9):
                    plausableKeysForSquare = []
                    for key in range(0, 9):
                        #print(self.theBoard.isLegalToPutNumInBox(num, self.theBoard.convertSquareAndKeyToX(square, key), self.theBoard.convertSquareAndKeyToY(square, key)))
                        if (self.guessingBoards[solvingBoardNumber].isLegalToPutNumInBox(num, self.guessingBoards[solvingBoardNumber].convertSquareAndKeyToX(square, key), self.guessingBoards[solvingBoardNumber].convertSquareAndKeyToY(square, key))):
                            plausableKeysForSquare.append(key)
                            #print(str(num) + "is valid for (" + str(self.theBoard.convertSquareAndKeyToX(square, key)) + ", " + str(self.theBoard.convertSquareAndKeyToY(square, key)) + ")"  )
                    if (len(plausableKeysForSquare) == 1):
                        self.guessingBoards[solvingBoardNumber].fillASquare(self.guessingBoards[solvingBoardNumber].convertSquareAndKeyToX(square, plausableKeysForSquare[0]), self.guessingBoards[solvingBoardNumber].convertSquareAndKeyToY(square, plausableKeysForSquare[0]), num) 
                        self.solvedSquares = self.solvedSquares + 1
            

    def forEachBoxCheckIfOnlyOneNumberCanWork(self, solvingBoardNumber):
        for y in range(0, 9):
            for x in range(0, 9):
                plausableNums = []
                for num in range(1, 10):
                    if self.guessingBoards[solvingBoardNumber].isLegalToPutNumInBox(num, x, y):
                        plausableNums.append(num)
                if len(plausableNums) == 1:
                    self.guessingBoards[solvingBoardNumber].fillASquare(x, y, plausableNums[0])
                    self.solvedSquares = self.solvedSquares + 1

    def solveBoard(self, solvingBoardNumber):
        solved = False
        pastNumberOfUnsolvedSquares = 81
        print('are we okay')
        while solved == False:
            entireTechniqueUnsolvedSquares = self.guessingBoards[solvingBoardNumber].getNumberOfUnsolvedSquares()
            pastNumberOfUnsolvedSquares = pastNumberOfUnsolvedSquares + 1

            while pastNumberOfUnsolvedSquares != self.guessingBoards[solvingBoardNumber].getNumberOfUnsolvedSquares():
                pastNumberOfUnsolvedSquares = self.guessingBoards[solvingBoardNumber].getNumberOfUnsolvedSquares()
                self.checkEachGroupIfOnlyOneSpotFitsForEachNumber(solvingBoardNumber)

            pastNumberOfUnsolvedSquares = pastNumberOfUnsolvedSquares + 1

            while pastNumberOfUnsolvedSquares != self.guessingBoards[solvingBoardNumber].getNumberOfUnsolvedSquares():
                pastNumberOfUnsolvedSquares = self.guessingBoards[solvingBoardNumber].getNumberOfUnsolvedSquares()
                self.forEachBoxCheckIfOnlyOneNumberCanWork(solvingBoardNumber)
            
            if self.guessingBoards[solvingBoardNumber].isBoardCompleted():
                solved = True
                self.theBoard = self.guessingBoards[solvingBoardNumber]
                print(str(solvingBoardNumber))
                return True
            if entireTechniqueUnsolvedSquares == self.guessingBoards[solvingBoardNumber].getNumberOfUnsolvedSquares():
                break

        if solved == False:
            #guesses will store all the squares that can be one of two numbers
            guesses = []
            #squares will store the coordinates of each piece in guesses
            squaresForGuesses = []
            for y in range(0, 9):
                for x in range(0, 9):
                    possibleValuesForSquare = self.guessingBoards[solvingBoardNumber].getPossibleValuesForSquare(x, y)
                    if len(possibleValuesForSquare) == 2:
                        guesses.append(possibleValuesForSquare)
                        squaresForGuesses.append([x, y])
            for pairIndex in range(0, len(guesses)):
                boardCopy = board.Board(self.guessingBoards[0].sets)
                for guessIndex in range(0, 2):
                    boardCopy.fillASquare(squaresForGuesses[pairIndex][0], squaresForGuesses[pairIndex][1], guesses[pairIndex][guessIndex])
                    self.guessingBoards.append(boardCopy)
                    return self.solveBoard(solvingBoardNumber + 1)
                    

            
            
        if solved == True:
            print("success! " + str(solvingBoardNumber))    
        return solved


        
    