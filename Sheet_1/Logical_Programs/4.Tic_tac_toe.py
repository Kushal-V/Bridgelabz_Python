import random

def createBoard():
    return [[" " for i in range(3)] for j in range(3)]

def printBoard(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end = " ")
        print()

def user(board):
    while True:
        userrow = int(input("Enter row to mark X: "))
        usercol = int(input("Enter column to mark X: "))
        if board[userrow][usercol] == " ":
            board[userrow][usercol] = "X"
            break
        else:
            print("Cell already occupied")
    return board

def computer(board):
    comp1 = random.randint(0,2)
    comp2 = random.randint(0,2)
    if board[comp1][comp2] == " ":
        board[comp1][comp2] = "O"
    else:
        computer(board)
    return board

def checkWin(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == "X" or board[i][0] == board[i][1] == board[i][2] == "O":
            return True
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == "X" or board[0][i] == board[1][i] == board[2][i] == "O":
            return True
    if board[0][0] == board[1][1] == board[2][2] == "X" or board[0][0] == board[1][1] == board[2][2] == "O":
        return True
    if board[0][2] == board[1][1] == board[2][0] == "X" or board[0][2] == board[1][1] == board[2][0] == "O":
        return True
    return False

def draw(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True

def ticTacToe():
    board = createBoard()
    while True:
        user(board)
        printBoard(board)
        if checkWin(board):
            print("User wins")
            break
        if draw(board):
            print("Draw")
            break
        computer(board)
        printBoard(board)
        if checkWin(board):
            print("Computer wins")
            break
        if draw(board):
            print("Draw")
            break

ticTacToe()
    
    