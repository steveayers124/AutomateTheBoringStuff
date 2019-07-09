# begin programming a game of Tic-Tac-Toe

def printboard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' ', }

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
