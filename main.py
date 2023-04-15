from Game import *

def main():
  player1 = Player("one", "X")  
  player2 = Player("two", "O")

  game = Game(player1, player2)
  while (game.winner == False and (not game.draw)):
    game.playGame()
  
  
if __name__=="__main__":
    main()