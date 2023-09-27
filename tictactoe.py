#Intro message
from time import *
print("Welcome to the Tic-Tac-Toe Game!")
#Create Board
board = ["-", "-", "-",
          "-", "-", "-",
            "-", "-", "-"]
current_player = "X"
winner = None
game_running = True

#Print board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])



#Player input
def playerInput(board):
    player_space = int(input("Choose a spot on the board to place your marking(1-9):"))
    if player_space >= 1 and player_space <= 9 and board[player_space-1] == "-":
        board[player_space-1] = current_player
        
    elif player_space >= 1 and player_space <= 9 and board[player_space-1] != "-":
        print("That spot is already taken, please input a different number!")
        playerInput(board)
    else:
        print("Please input a number inbetween 1-9!")
        playerInput(board)

#Check for win
def horizontalWin(board):
    global winner
    if (board[0] == board[1] == board[2]) and board[1] != "-":
        winner = board[1]
        return True
    elif (board[3] == board[4] == board[5]) and board[4] != "-":
        winner = board[4]
        return  True
    elif (board[6] == board[7] == board[8]) and board[7] != "-":
        winner = board[7]
        return True

def verticalWin(board):
    global winner
    if (board[0] == board[3] == board[6]) and board[3] != "-":
        winner = board[3]
        return True
    elif (board[1] == board[4] == board[7]) and board[4] != "-":
        winner = board[4]
        return True
    elif (board[2] == board[5] == board[8]) and board[5] != "-":
        winner = board[5]
        return True

def diagonalWin(board):
    global winner
    if (board[0] == board[4] == board[8]) and board[4] != "-":
        winner = board[4]
        return True
    elif (board[2] == board[4] == board[6]) and board[4] != "-":
        winner = board[4]
        return True

#Check for tie
def checkTie(board):
    global game_running
    if (horizontalWin(board) and verticalWin(board) and diagonalWin(board)) == False:
        print("This game was a Tie! Press P to play again.")
        game_running = False

def checkWin():
    global game_running
    global winner
    if horizontalWin(board)  or verticalWin(board) or diagonalWin(board):
        print(f"The winner is {winner}!")
        game_running = False

        

#Switch player
def playerSwitch():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

while game_running:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    playerSwitch()
    