class Board():
#board class that represets the tic tac toe board 

    #board init: 3x3 list 
    def __init__(self):
        self.board = [["-", "-", "-"],
                      ["-", "-", "-"],
                      ["-", "-", "-"]
                      ]
        

    def __str__(self):
        #function to override print and print the board
        return f'{self.board[0][0]} {self.board[0][1]} {self.board[0][2]}\n{self.board[1][0]} {self.board[1][1]} {self.board[1][2]}\n{self.board[2][0]} {self.board[2][1]} {self.board[2][2]}'

    def isValidMove(self,row,col):
      #returns true if the move is valid
      return (self.board[row][col] == "-")
      
    def draw(self):
      #iterates throughout the board list and returns true if there are no more availiable squares, hence it is a draw
      for row in range(len(self.board)):
        for col in range(len(self.board)):
          if(self.board[row][col] == "-"):
            return False
      return True
    
    def checkWin(self):
      #function to check if there is a winning condition

      l = len(self.board)

      # the following spits the 2d list into its respective diagnals,rows,and columns
      diagnalOne = [self.board[i][i] for i in range(l)]
      diagnalTwo = [self.board[l-1-i][i] for i in range(l-1, -1, -1)]

      row0 = self.board[0]
      row1 = self.board[1]
      row2 = self.board[2]

      col0 = [symbol[0] for symbol in self.board]
      col1 = [symbol[1] for symbol in self.board]
      col2 = [symbol[2] for symbol in self.board]
      
      #converts the split up lists into a set, if the length of the set is 1 that means all elements are the same hence there is a winning condition
      if (diagnalOne[0] != "-" and  (len(set(diagnalOne)) == 1)):
        return True
      elif (diagnalTwo[0] != "-" and len(set(diagnalTwo)) == 1):
          return True
      elif (row0[0] != "-" and (len(set(row0)) == 1)):
        return True
      elif (row1[0] != "-" and (len(set(row1)) == 1)):
        return True
      elif (row2[0] != "-" and (len(set(row2)) == 1)):
        return True
      elif (col0[0] != "-" and (len(set(col0)) == 1)):
        return True
      elif (col1[0] != "-" and (len(set(col1)) == 1)):
        return True
      elif (col2[0] != "-" and (len(set(col2)) == 1)):
        return True
      else:
        return False

    #sets the board at a specfic colummn and row to a value
    def setSquare(self,row, col,value):
        self.board[row][col] = value

    #retruns true if the board has no values
    def isEmpty(self):

      #splits the board into indvidual sets and find the union of these sets
      my_set = set.union(*map(set, self.board))

      #if the uinon set has a length of one that means all elements are the same hence it is empty 
      if(len(my_set) == 1):
        return True
      return False

    #function to clear the board 
    def clearBoard(self):

      #iterates throughout the whole board and sets all values of the list to "-"
      for row in range(len(self.board)):
        for col in range(len(self.board)):
          self.board[row][col] = "-"
    





      

      

