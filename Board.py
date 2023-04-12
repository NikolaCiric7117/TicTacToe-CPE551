class Board():
    def __init__(self):
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]
                      ]

    def __str__(self):
        return f'{self.board[0][0]} {self.board[0][1]} {self.board[0][2]}\n{self.board[1][0]} {self.board[1][1]} {self.board[1][2]}\n{self.board[2][0]} {self.board[2][1]} {self.board[2][2]}'

    def isValidMove(self,row,col):
      return (row>=0 and col<=2) and (row>=0 and col<=2) and (self.board[row][col] == 0)
    
    def draw(self):
      for row in range(0,len(self.board)):
        for col in range(0,len(self.board[0])):
          if (self.board[row][col] == 0):
             return True
      return False
    
    def checkWin(self):
      #first diagnals
      if(self.board[1][1] != 0 and (self.board[1][1] == self.board[0][0]) and (self.board[1][1]==self.board[2][2])):
        return True 
      if(self.board[1][1] !=0 and (self.board[1][1] == self.board[0][2]) and (self.board[1][1]==self.board[2][0])):
        return True 
      
      #check vertical
      for row in range(len(self.board)):
        value  = self.board[0][row]
        win = True
        for col in range(1,len(self.board)):
          if(value != self.board[row][col]):
            win = False
            break

          if(win):
            return True
      
      #check  horizontal
      for col in range(len(self.board)):
        value  = self.board[col][0]
        win = True
        for row in range(1, len(self.board)):
          if(value != self.board[col][row]):
            win = False
            break
          if (win):
            return True
      
      return False 
      
    def setSquare(self,row, col,value):
        self.board[row][col] = value







      

      

