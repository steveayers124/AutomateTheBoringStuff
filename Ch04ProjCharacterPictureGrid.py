# Given a list of lists having one character per item,
#  print every character in the lists in order to produce a picture.

def printStringGrid(grid):
    for i in grid:
        for j in i:
            print(str(j)[0], end='')
        print('')

def printCharacterGrid(grid):
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            print(str(grid[j][i])[0], end='')
        print('')

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
# printCharacterGrid(grid)

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
printCharacterGrid(grid)
