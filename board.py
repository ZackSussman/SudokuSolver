import TestingSets

class Board(): 

    sets = []

    def __init__(self):
        #store 27 sets of 9 initially all 0
        #each set refers to a range of 9 values which must satisfy sudoku rules
        for row in range(0, 27):
            subset = []
            for num in range(0, 9):
                subset.append(0)
            self.sets.append(subset)

    #rounds a number up to 3, 6, or 9, used for determining box space
    def roundUpToMultipleOfThree(self, val): 
        if val < 3:
            return 3
        if val < 6:
            return 6
        if val < 9:
            return 9

    def printSets(self):
        n = 0
        for row in self.sets:
            if (n%9 == 0):
                print()
            print(row)
            n = n + 1
            

    def isBoxEmpty(self, x, y):
        if (self.sets[y][x] == 0):
            return True
        return False

    def doesRowHaveN(self, row, n):
        for number in self.sets[row]:
            if (number == n):
                return True
        return False

    def doesCollumnHaveN(self, collumn, n):
        for number in self.sets[9+collumn]:
            if (number == n):
                return True
        return False

    def doesSquareHaveN(self, square, n):
        for number in self.sets[18 + square]:
            if (number == n):
                return True
        return False

    def getNumberOfUnsolvedSquares(self):
        number = 0
        for y in range(0, 9):
            for x in range(0, 9):
                if self.isBoxEmpty(x, y):
                    number = number + 1
        return number

    def isRowValid(self, row):
        for i in range(1, 10):
            if (self.sets[row][i-1].count(i) > 1):
                return False
        return True

    def isCollumnValid(self, collumn):
        for i in range(1, 10):
            if (self.sets[collumn + 9][i-1].count(i) > 1):
                return False
        return True
    
    def isSquareValid(self, square):
        for i in range(1, 10):
            if (self.sets[square + 18][i-1].count(i) > 1):
                return False
        return True

    def isLegalToPutNumInBox(self, num, x, y):
        
        #check if the box already has a number in it
        if (self.isBoxEmpty(x, y) == False):
            return False

        #check if the row contains num
        if (self.sets[y].count(num) > 0):
            return False
        
        #check if the collumn contains num
        if (self.sets[x+9].count(num) > 0):
            return False

        #check if the box contains num
        if (self.sets[18 + self.convertPointToSquare(x, y)].count(num) > 0):
            return False
         
        return True

    def convertPointToSquare(self, x, y):
        square = 0
        for yTester in range(3, 10, 3):
            for xTester in range(3, 10, 3):
                if (self.roundUpToMultipleOfThree(x) == xTester and self.roundUpToMultipleOfThree(y) == yTester):
                    return square
                square = square + 1

    def convertSquareAndKeyToX(self, square, key):
        return 3*(square % 3) + (key % 3)

    def convertSquareAndKeyToY(self, square, key):
        return (square//3)*3 + key//3

    #fills all the pieces in sets which are the given square with the given value
    def fillASquare(self, x, y, val):
        if (val == ''):
            val = 0
        else:
            val = int(val)
        self.sets[y][x] = val #fill this value into its row space
        self.sets[x + 9][y] = val #fill this value into its collumn space
        #fill this value into the box space
        box = 0
        for yTester in range(3, 10, 3):
            for xTester in range(3, 10, 3):
                if (self.roundUpToMultipleOfThree(x) == xTester and self.roundUpToMultipleOfThree(y) == yTester):
                    self.sets[18 + box][ 3*(y%3) + (x%3) ] = val
                box = box + 1



