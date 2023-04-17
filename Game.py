from Board import *
from Player import *
class Game():
    #game class is the main driving class which will play Tic Tac Toe and find a winner

    def __init__(self, player1, player2):

        #constructor to set up the player, board, win,draw,and move count
        self.player1 = Player("one", "X")
        self.player2 = Player("two", "O")
        self.board = Board()

        #intializes the winner and draw to false meaning the game is not over 
        self.winner = False
        self.draw = False

        #counts the move, used to figure out which player goes next
        self.moveCount = 1
        
    #function that plays tic tac toe
    def playGame(self,row,col):
        
        #first figure out who goes first using move count. If the movecount is even player 1 turn
        if (self.moveCount %2 ==0):
            #checks if the move is valid
            if ( self.board.isValidMove(row, col)==True):

                #sets the board at a given square to player 1 symbol
                self.board.setSquare(row, col, self.player1.symbol)
                print(self.board, "\n")

                #checks if there is a winning condition on the board and if so sets the winnner flag to true
                if (self.board.checkWin() == True):
                    print(self.board)
                    print("Player one won!")
                    self.winner = True
            else:
                print("Please enter a valid input")

        #same thing for player 2
        else:
            if (self.board.isValidMove(row, col)):
                self.board.setSquare(row, col, self.player2.symbol)
                print(self.board, "\n")
                if (self.board.checkWin() == True):
                    print(self.board)
                    print("Player two won!")
                    self.winner = True
            else :
              print("Please enter a valid input ")

        #checks to see if there is a draw and if so set the draw flag to true      
        if (self.board.isEmpty() == False and self.board.draw() == True and self.board.checkWin()==False):
          print("Draw")
          self.draw = True
          return


      



  