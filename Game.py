from Board import *
from Player import *


class Game():

    def __init__(self, player1, player2):
        self.player1 = Player("one", "X")
        self.player2 = Player("two", "O")
        self.board = Board()
        self.winner = False
        self.moveCount = 1
        

    def playGame(self):
        print(self.board, "\n")
        row = 0
        col = 0

        if (self.moveCount %2 !=0):
            row, col = map(int, input("Player one move: ").split())
            if ( self.board.isValidMove(row, col)==True):
                self.board.setSquare(row, col, self.player1.symbol)
                self.moveCount = self.moveCount +1
                if (self.board.checkWin() == True):
                    print(self.board)
                    print("Player one won!")
                    self.winner = True
            else:
                print("Please enter a valid input")

        else:
            row, col = map(int, input("Player two move: ").split())
            if (self.board.isValidMove(row, col)):
                self.board.setSquare(row, col, self.player2.symbol)
                self.moveCount = self.moveCount + 1
                if (self.board.checkWin() == True):
                    print(self.board)
                    print("Player two won!")
                    self.winner = True
            else :
              print("Please enter a valid input ")


