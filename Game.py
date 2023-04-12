from queue import Empty
import Board
from Board import *
from Player import *

class Game():

  def __init__(self,player1,player2):
    self.player1 = Player("one","X")
    self.player2 = Player("two","O")
    self.board = Board()
    self.winner = False
    self.player1First = True

  def playGame(self):
    print(self.board,"\n")
    row = 0
    col = 0

    if(self.player1First==True) :
      row,col = map(int,input("Player one move: ").split())
      if(self.board.isValidMove(row,col)):
        self.board.setSquare(row,col,self.player1.symbol)
        self.player1First = False
        if(self.board.checkWin() == True):
          print("Player one won!")
          
    else:
      row, col = map(int, input("Player two move: ").split())
      if (self.board.isValidMove(row, col)):
        self.board.setSquare(row, col, self.player2.symbol)
        self.player1First = True
        if (self.board.checkWin() == True):
          print("Player two won!")

          
   
          
        
          
          

          

    
      
    
    
      
    
        

      
      
      
      
one = Player("one", "X")
two = Player("two", "O")
game = Game(one,two)
while(game.winner==False):
    game.playGame()





      
      






