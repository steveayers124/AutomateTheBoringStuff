# begin programming a game of Tic-Tac-Toe

def printboard(board):
    print(board['A3'] + '|' + board['B3'] + '|' + board['C3'])
    print('-+-+-')
    print(board['A2'] + '|' + board['B2'] + '|' + board['C2'])
    print('-+-+-')
    print(board['A1'] + '|' + board['B1'] + '|' + board['C1'])


theBoard = {'A3': ' ', 'B3': ' ', 'C3': ' ',
            'A2': ' ', 'B2': ' ', 'C2': ' ',
            'A1': ' ', 'B1': ' ', 'C1': ' ', }

turn = 'X'
for i in range(9):
    printboard(theBoard)
    move = input('Turn for ' + turn + '. Move on which space?')
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printboard(theBoard)

# theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
#             'mid-L': ' ', 'mid-M': 'X', 'mid-R': ' ',
#             'low-L': ' ', 'low-M': ' ', 'low-R': ' ', }
# printboard(theBoard)
#
# theBoard = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O',
#             'mid-L': 'X', 'mid-M': 'X', 'mid-R': ' ',
#             'low-L': ' ', 'low-M': ' ', 'low-R': 'X', }
# printboard(theBoard)
