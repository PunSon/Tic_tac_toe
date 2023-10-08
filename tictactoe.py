import sys
#Intro message
print("Welcome to the Tic-Tac-Toe Game!")

#Create Board
board = ["-", "-", "-",
          "-", "-", "-",
            "-", "-", "-"]

#Create a winner and a game running variable to set the structure of the game
winner = None
game_running = True

#Print board
def displayBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

#Inputs user for whether they want to choose X or O as their game piece
def gamePiece():
    global current_player
    player_option = input("Select X or O:")
    print("Great! Player 1 is",player_option.upper())
    if player_option.upper() == "X":
        current_player = "X"
    elif player_option.upper() == "O":
        current_player = "O"
    else:
        print("Please enter either X or O!")
        gamePiece()

#Asks player for where they want to play their game piece and prints a new board with updated markings
def playerInput(board):
    player_space = input("Choose a spot on the board to place your marking(1-9):")
    if player_space == "q":
        sys.exit("You quit the game.")
    
    try:
        player_space = int(player_space)
        if player_space >= 1 and player_space <= 9 and board[player_space-1] == "-":
            board[player_space-1] = current_player   
        elif player_space >= 1 and player_space <= 9 and board[player_space-1] != "-":
            print("That spot is already taken, please input a different number!")
            playerInput(board)   
        else:
            print("Please input a number inbetween 1-9!")
            playerInput(board)
    except ValueError:
        print("Invalid input. Please input a number between 1-9 or press 'q' to quit.")
        playerInput(board)

#Checks to see if 3 game pieces are aligned horizontally
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

#Checks to see if 3 game pieces are aligned vertically
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

#Checks to see if 3 game pieces are aligned diagonally
def diagonalWin(board):
    global winner
    if (board[0] == board[4] == board[8]) and board[4] != "-":
        winner = board[4]
        return True
    elif (board[2] == board[4] == board[6]) and board[4] != "-":
        winner = board[4]
        return True

#Checks for tie
def checkTie(board):
    global game_running
    if (winner == None) and all(cell != "-" for cell in board):
        print("This game was a Tie!")
        game_running = False

#Checks to see if either the horizontal/vertical/diagonal win conditions were true
def checkWin():
    global game_running
    global winner
    if horizontalWin(board)  or verticalWin(board) or diagonalWin(board):
        print(f"The winner is {winner}!")
        game_running = False        

#Switches player when an input is entered
def playerSwitch():
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

#Initially asks for what piece the user wants to be(this is only run once)
gamePiece()

#Continuously runs the game until there is a win
while game_running:
    displayBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    playerSwitch()

    