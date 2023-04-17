
import tkinter as tk
import tkinter.messagebox 
from Game import *

class Gui():
  #GUI class to visualize the tic tac toe game

  def __init__(self,master):
    #initalizes a new game
    player1 = Player("one","X")
    player2 = Player("two", "X")
    self.game = Game(player1,player2)


    #initalizes the GUI window
    self.master = master
    master.title("TicTacToe")
    frame = tk.Frame(master=master)
    frame.pack(pady=10)
    self.label = tk.Label(master=frame, text="Tic Tac Toe")
    self.label.pack()

    #initalzies a frame in the master window where buttons can be created
    self.frame1 = tk.Frame(master=master, borderwidth=2)
    self.frame1.pack(padx=10, pady=10)

    #The following sets up 9 buttons which will represent the tic tac toe squares of the board, when the button is clicked it will call the buttonClick() function
    self.button1 = tk.Button(master=self.frame1, width=10, height=5, command=lambda:  self.buttonClick(1))
    self.button1.grid(row=0, column=0, padx=5, pady=5)

    self.button2 = tk.Button(master=self.frame1, width=10, height=5, command=lambda:  self.buttonClick(2))
    self.button2.grid(row=0, column=1, padx=5, pady=5)

    self.button3 = tk.Button(master= self.frame1,  width=10, height=5, command=lambda:  self.buttonClick(3))
    self.button3.grid(row=0, column=2, padx=5, pady=5)

    self.button4 = tk.Button(master= self.frame1,  width=10, height=5, command=lambda: self.buttonClick(4))
    self.button4.grid(row=1, column=0, padx=5, pady=5)

    self.button5 = tk.Button(master= self.frame1,  width=10, height=5, command=lambda: self.buttonClick(5))
    self.button5.grid(row=1, column=1, padx=5, pady=5)

    self.button6 = tk.Button(master=self.frame1,  width=10, height=5, command=lambda: self.buttonClick(6))
    self.button6.grid(row=1, column=2, padx=5, pady=5)

    self.button7 = tk.Button(master=self.frame1,  width=10, height=5, command=lambda: self.buttonClick(7))
    self.button7.grid(row=2, column=0, padx=5, pady=5)

    self.button8 = tk.Button(master=self.frame1,  width=10, height=5, command=lambda:  self.buttonClick(8))
    self.button8.grid(row=2, column=1, padx=5, pady=5)

    self.button9 = tk.Button(master=self.frame1,  width=10, height=5, command=lambda:  self.buttonClick(9))
    self.button9.grid(row=2, column=2, padx=5, pady=5)

    #initalizes another frame in the master window where the restart button will be 
    self.restartFrame = tk.Frame(master = master, border = 2)
    self.restartFrame.pack()

    #sets up the restart button
    self.restartButton = tk.Button(master = self.restartFrame,text = "Restart",state=tk.DISABLED, width=10,height=3,command=lambda:self.restart())
    self.restartButton.grid(row =0,column=1,padx=10,pady=10)

  #function that decides what to do on button click, takes in one parameter that respensnt which button was clicked
  def buttonClick(self,x):

    #the following if statemts are all the same, on thing that differnt is checks what button is pressed and changes that corresponding buttons text
    if(x==1):

      #button 1 is in column 0 and row zero of the board list
      row,col = 0,0

      #checks if the move is valid
      if (self.game.board.isValidMove(row, col) == False):
        tkinter.messagebox.showinfo("Tic Tac Toe", "Please enter a valid move")
      else:
      #checks what player is up using the moveCount from the game object and if player one, sets the coresponding buttons text to player 1 sysmbol
        if(self.game.moveCount%2!=0):
          self.button1["text"] = self.game.player1.symbol
        else:
          self.button1["text"] = self.game.player2.symbol

        self.game.moveCount += 1

      #calls the game function to play tic tac toe
        self.game.playGame(row,col)
  
    if(x==2):
      row,col = 0,1
      if (self.game.board.isValidMove(row, col) == False):
        tkinter.messagebox.showinfo("Tic Tac Toe", "Please enter a valid move")
      else:
        if (self.game.moveCount % 2 != 0):
          self.button2["text"] = self.game.player1.symbol
        else:
          self.button2["text"] = self.game.player2.symbol
        self.game.moveCount += 1
        self.game.playGame(row,col)
     
      
    if (x == 3):
      row,col = 0,2

      if (self.game.board.isValidMove(row, col) == False):
        tkinter.messagebox.showinfo("Tic Tac Toe", "Please enter a valid move")
      else:
        if (self.game.moveCount % 2 != 0):
          self.button3["text"] = self.game.player1.symbol
        else:
          self.button3["text"] = self.game.player2.symbol
        self.game.moveCount += 1
        self.game.playGame(row, col)
      
    if (x == 4):
      row, col = 1, 0
      if (self.game.board.isValidMove(row, col) == False):
        tkinter.messagebox.showinfo("Tic Tac Toe", "Please enter a valid move")
      else:
        if (self.game.moveCount % 2 != 0):
          self.button4["text"] = self.game.player1.symbol
        else:
          self.button4["text"] = self.game.player2.symbol
        self.game.moveCount += 1
        self.game.playGame(row, col)
      
    if (x == 5):
      row, col = 1, 1
      if (self.game.board.isValidMove(row, col) == False):
        tkinter.messagebox.showinfo("Tic Tac Toe", "Please enter a valid move")
      else:
        if (self.game.moveCount % 2 != 0):
          self.button5["text"] = self.game.player1.symbol
        else:
          self.button5["text"] = self.game.player2.symbol
        self.game.moveCount += 1
        self.game.playGame(row, col)
      
    if (x == 6):
      row, col = 1, 2
      if (self.game.board.isValidMove(row, col) == False):
        tkinter.messagebox.showinfo("Tic Tac Toe", "Please enter a valid move")
      else:
        if (self.game.moveCount % 2 != 0):
          self.button6["text"] = self.game.player1.symbol
        else:
          self.button6["text"] = self.game.player2.symbol
        self.game.moveCount += 1
        self.game.playGame(row, col)
      
    if (x == 7):
      row, col = 2, 0
      if (self.game.board.isValidMove(row, col) == False):
        tkinter.messagebox.showinfo("Tic Tac Toe", "Please enter a valid move")
      else:
        if (self.game.moveCount % 2 != 0):
          self.button7["text"] = self.game.player1.symbol
        else:
          self.button7["text"] = self.game.player2.symbol
        self.game.moveCount += 1
        self.game.playGame(row, col)
      
    if (x == 8):
      row, col = 2, 1
      if (self.game.board.isValidMove(row, col) == False):
        tkinter.messagebox.showinfo("Tic Tac Toe", "Please enter a valid move")
      else:
        if (self.game.moveCount % 2 != 0):
          self.button8["text"] = self.game.player1.symbol
        else:
          self.button8["text"] = self.game.player2.symbol
        self.game.moveCount += 1
        self.game.playGame(row, col)

    if (x == 9):
      row, col = 2, 2
      if (self.game.board.isValidMove(row, col) == False):
        tkinter.messagebox.showinfo("Tic Tac Toe", "Please enter a valid move")
      else:
        if (self.game.moveCount % 2 != 0):
          self.button9["text"] = self.game.player1.symbol
        else:
          self.button9["text"] = self.game.player2.symbol
        self.game.moveCount += 1
        self.game.playGame(row, col)
     
    #checks if there is a winner on each button click using the game winner flag 
    if(self.game.winner == True):

      #disable all buttons so no moves can be made
      self.disableButtons()

      #uses the moveCount from the game object to decide what player has won
      if(self.game.moveCount %2 ==0):
        tkinter.messagebox.showinfo("Tic Tac Toe", "Player one wins")

        #upon a win the restart button is enabled 
        self.restartButton["state"] = tk.NORMAL
      else:
        tkinter.messagebox.showinfo("Tic Tac Toe", "Player two wins")
        self.restartButton["state"] = tk.NORMAL

    #checks if there is a draw using the game draw flag
    if(self.game.draw == True):
      self.disableButtons()
      tkinter.messagebox.showinfo("Tic Tac Toe", "Draw")
      self.restartButton["state"] = tk.NORMAL

  #function to diable all buttons
  def disableButtons(self):
    self.button1["state"] = tk.DISABLED
    self.button2["state"] = tk.DISABLED
    self.button3["state"] = tk.DISABLED
    self.button4["state"] = tk.DISABLED
    self.button5["state"] = tk.DISABLED
    self.button6["state"] = tk.DISABLED
    self.button7["state"] = tk.DISABLED
    self.button8["state"] = tk.DISABLED
    self.button9["state"] = tk.DISABLED
  
  #function for the restart button
  def restart(self):

    #clears the board and sets all flags and move count of the board to default values 
    self.game.board.clearBoard()
    self.game.winner = False
    self.game.draw = False
    self.game.moveCount = 1

    #disables the restart value, upon a new a game
    self.restartButton["state"]= tk.DISABLED

    #sets all button texts to blank
    self.button1["text"] = " "
    self.button2["text"] = " "
    self.button3["text"] = " "
    self.button4["text"] = " "
    self.button5["text"] = " "
    self.button6["text"] = " "
    self.button7["text"] = " "
    self.button8["text"] = " "
    self.button9["text"] = " "

    #enables all buttons
    self.button1["state"] = tk.NORMAL
    self.button2["state"] = tk.NORMAL
    self.button3["state"] = tk.NORMAL
    self.button4["state"] = tk.NORMAL
    self.button5["state"] = tk.NORMAL
    self.button6["state"] = tk.NORMAL
    self.button7["state"] = tk.NORMAL
    self.button8["state"] = tk.NORMAL
    self.button9["state"] = tk.NORMAL

    
    
    
      
        










