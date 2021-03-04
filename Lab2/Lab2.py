

class Sudoku:
    def __init__(self, name):
        self.name = name
        self.grid = [[0 for x in range(9)] for y in range(9)]
    
    def addRow(self, row, data):
        for column in range(0, 9):
            number =  data[0][column]
            self.grid[row][column] = number
       
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





      

#solve, backtracking
#find empty space
#test if number is approved
#print sudoku

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
    for x in sudokus:
        x.print()

    #loop the list of sudokus, solve them and print them
    #capture time



if __name__=="__main__": 
    main() 
