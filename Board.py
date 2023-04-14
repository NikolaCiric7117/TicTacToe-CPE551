class Board():
    def __init__(self):
        self.board = [["-", "-", "-"],
                      ["-", "-", "-"],
                      ["-", "-", "-"]
                      ]
        

    def __str__(self):
        return f'{self.board[0][0]} {self.board[0][1]} {self.board[0][2]}\n{self.board[1][0]} {self.board[1][1]} {self.board[1][2]}\n{self.board[2][0]} {self.board[2][1]} {self.board[2][2]}'

    def isValidMove(self,row,col):
      return (row>=0 and col<=2) and (row>=0 and col<=2) and (self.board[row][col] == "-")
    
    
    def checkWin(self):
      l = len(self.board)
      diagnalOne = [self.board[i][i] for i in range(l)]
      diagnalTwo = [self.board[l-1-i][i] for i in range(l-1, -1, -1)]

      row0 = self.board[0]
      row1 = self.board[1]
      row2 = self.board[2]

      col0 = [symbol[0] for symbol in self.board]
      col1 = [symbol[1] for symbol in self.board]
      col2 = [symbol[2] for symbol in self.board]
      
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
  
    def setSquare(self,row, col,value):
        self.board[row][col] = value
    
    def isEmpty(self):
      my_set = set.union(*map(set, self.board))
      if(len(my_set) == 1):
        return True
      return False
    





      

      

