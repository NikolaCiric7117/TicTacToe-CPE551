from Board import *
from Player import *


class Game():

    def __init__(self, player1, player2):
        self.player1 = Player("one", "X")
        self.player2 = Player("two", "O")
        self.board = Board()
        self.winner = False
        self.draw = False
        self.moveCount = 1
        

    def playGame(self,row,col):
        

        if (self.moveCount %2 ==0):
            if ( self.board.isValidMove(row, col)==True):
                self.board.setSquare(row, col, self.player1.symbol)
                print(self.board, "\n")
                if (self.board.checkWin() == True):
                    print(self.board)
                    print("Player one won!")
                    self.winner = True
            else:
                print("Please enter a valid input")

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
        if (self.board.isEmpty() == False and self.board.draw() == True and self.board.checkWin()==False):
          print("Draw")
          self.draw = True
          return


      



  