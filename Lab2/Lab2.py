import time

class Sudoku:
    def __init__(self, name):
        self.name = name
        self.grid = [[0 for x in range(9)] for y in range(9)]
          
    def addRow(self, row, data):
        for column in range(0, 9):
            number =  data[0][column]
            self.grid[row][column] = int(number)

    def getCelltoSolve(self):
        for x in range(len(self.grid)):
            for c in range(len(self.grid)):
                if self.grid[x][c] is 0:
                    return x, c
        return False

    def solve(self):     
        if self.getCelltoSolve() is False:
            return True
        row, column = self.getCelltoSolve()
        self.val = self.getAllowValues(row, column)
        for x in self.val:
            self.grid[row][column] = x
            if self.solve() is True:
                return True
            self.grid[row][column]= 0
        return False

    def checkRow(self,row, value):
        return all([value != self.grid[row][x] for x in range(9)])

    def checkColumn(self,column, value):
        return all([value != self.grid[x][column] for x in range(9)])

    def checkMatrix(self,row, column, value):
         secTopX, secTopY = 3*(row//3), 3*(column//3)
         for x in range(secTopX, secTopX + 3):
            for y in range(secTopY, secTopY + 3):
                if self.grid[x][y] == value:
                    return False 
         return True
                
    def getAllowValues(self,i, j):
       values = []
       for x in range(1, 10):
          if self.checkRow(i,x): 
            if self.checkColumn(j,x):
               if self.checkMatrix(i, j, x):
                    values.append(x)      
       return values

    def print(self):
        print(self.name)
        print("-"*27)
        for r in range(len(self.grid)):
            row = ""
            for c in range(len(self.grid[r])):
                if c%3 == 0:
                    row += "|"
                row += " "+str(self.grid[r][c])
                if c%3 == 2:
                    row += " |"
            print(row)
            if r % 3 == 2:
               print("-"*27)
        print('\n')    


def main():
    sudokus = []
    
    def createSudoku(nr):
        sudokus.append(Sudoku('SUDOKU' + ' ' + str(nr)))
        return (nr - 1)

    #read file
    def retrieveItemsFromFile():
        with open("sudoku.txt", "r") as sudoku:
            content = sudoku.read().splitlines()
            sudokuNr = 0
            for x in range(0, 10): 
                sudokuNr = sudokuNr + 1
                j = content.index('SUDOKU ' + str(sudokuNr)) + 1    
                index = createSudoku(sudokuNr)            
                for i in range(0, 9):                
                    itemInfo = content[j].split()
                    sudokus[index].addRow(i, itemInfo)
                    j = j + 1
                
    retrieveItemsFromFile() 
    t = time.process_time()
    for x in sudokus:
      x.solve()
    elapsedTime = time.process_time() - t
    print('Time:', elapsedTime)
    for x in sudokus:
      x.print()

if __name__=="__main__": 
    main() 
