import fileinput
import numpy as np

def parse():
    numbers = []

    boards = []
    board = []

    for line in fileinput.input():
        if numbers == []:
            numbers = line.split(',')

        else:
            l = line.strip()
            if l == '' and board != []:
                boards.append(np.array(board))
                board = []
            elif l.strip() != '':
                board.append(l.split())

    boards.append(board)

    return numbers, boards


def task1(numbers, boards):
    markers = []
    for board in boards:
        markers.append([[[x, False] for x in row] for row in board ])

    for number in numbers:
        for board in markers:

            mark(number, board)

            if checkIfWinner(board):
                return int(number) * sumNotMarked(board)



def mark(number, board):
    for row in board:
        for col in row:
            if col[0] == number:
                col[1] = True

def sumNotMarked(board):
    res = 0

    for row in board:
        for col in row:
            if col[1] == False:
                res += int(col[0])
    return res




def checkIfWinner(board):
    required = len(board[0])


    rotated = np.rot90(board)

    for row in rotated:
        if list(map(lambda x: x[1], row)).count('True') == required:
            return True


    for row in board:
        if list(map(lambda x: x[1], row)).count(True) == required:
            return True



def task2(numbers, boards):
    winners = []

    markers = []
    for board in boards:
        markers.append([[[x, False] for x in row] for row in board ])

    for number in numbers:
        for board in markers:

            mark(number, board)

            if checkIfWinner(board):
                if board not in winners:
                    winners.append(board)

                if len(winners) == len(boards):

                    return int(number) * sumNotMarked(board)

numbers, boards = parse()

print(task1(numbers, boards))
print(task2(numbers, boards))
