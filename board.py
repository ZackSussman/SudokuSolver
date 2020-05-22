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
        for row in self.sets:
            print(row)

    #fills all the pieces in sets which are the given square with the given value
    def fillASquare(self, x, y, val):
        self.sets[y][x] = val #fill this value into its row space
        self.sets[x + 9][y] = val #fill this value into its collumn space
        #fill this value into the box space
        box = 0
        for yTester in range(3, 10, 3):
            for xTester in range(3, 10, 3):
                if (self.roundUpToMultipleOfThree(x) == xTester and self.roundUpToMultipleOfThree(y) == yTester):
                    self.sets[18 + box][ 3*(y%3) + (x%3) ] = val
                box = box + 1

