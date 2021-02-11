##Tic Tac Toe
#Name:
#Date:

#1. (Var) Setup the empty board as a list
theBoard = [' ']*10

#2. (fun) Print the board.
#in: a 10 item list (either x, o or ' ')
#do: print a graphic for the board
#out: none

def printBoard(board):
    print(" "+board[7]+" | "+board[8]+" | "+board[9])
    print("---+---+---")
    print(" "+board[4]+" | "+board[5]+" | "+board[6])
    print("---+---+---")
    print(" "+board[1]+" | "+board[2]+" | "+board[3])
    
#printBoard(theBoard)

#3a. (fun) Determine if player is X or O
player1 = ''
player2 = ''

#in: None
#do: get user choice, assign X/O to player1 and 2
#out: None

def chooseLetter():
  global player1
  global player2

  while True:
    choice = input("P1 would you like to be X or O? ").lower()

    if choice == 'x': 
      player1 = 'X'
      player2 = 'O'
      return
    elif choice == 'o':
      player1 = 'O'
      player2 = 'X'
      return

#chooseLetter()
    


#3b. (fun) Choose starting player 1 or 2
def chooseStart():
    pass

#4. (fun) Get player move
#in: board as list, player as X or O
#do: get user choice (1-9),
#    check if the space is empty,
#    update the board with the X or O at the user location
#out: none

def playerMove(board, player):
    pass


#5. (fun) Check Winner
#in: board as list, player as X or O
#do: check all possible win scenarios
#out: True for win, False otherwise
    
def checkWin(board, player):
    pass


#6. (fun) Check if board is full
#Because there are 10 list items for 9 spots,
#the first item theBoard[0] will always be ' '
#in: board as list
#do: count number of empty spaces, if there is no more spaces
#out: return True if board is full, False otherwise

def checkFull(board):
    pass

#7. Main function

def main():
    #print Welcome
    #print instructions

    #game play
    #get player letter choice
    
    #while board is not full
    ###first player move
        #player chooses move
        #print board
        #check win
        #check board full

    ###second player move
        #player chooses move
        #print baord
        #check win
    
    
    pass

