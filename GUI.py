
import tkinter as tk
import tkinter.messagebox 
from tkinter.tix import COLUMN
from Game import *

class Gui():

  def __init__(self,master):
    #Game init
    player1 = Player("one","X")
    player2 = Player("two", "X")
    self.game = Game(player1,player2)


    #Gui init
    self.master = master
    master.title("TicTacToe")
    frame = tk.Frame(master=master)


    frame.pack(pady=10)

    self.label = tk.Label(master=frame, text="Tic Tac Toe")
    self.label.pack()

    self.frame1 = tk.Frame(master=master, borderwidth=2)
    self.frame1.pack(padx=10, pady=10)
    self.button1 = tk.Button(master=self.frame1, text='', width=10,
                             height=5, bg='white', command=lambda:  self.buttonClick(1))


    self.button1.grid(row=0, column=0, padx=5, pady=5)

    self.button2 = tk.Button(master=self.frame1, width=10, height=5,
                             bg='white', command=lambda:  self.buttonClick(2))
    self.button2.grid(row=0, column=1, padx=5, pady=5)

    self.button3 = tk.Button(master= self.frame1,  width=10, height=5,
                             bg='white', command=lambda:  self.buttonClick(3))
    self.button3.grid(row=0, column=2, padx=5, pady=5)

    self.button4 = tk.Button(master= self.frame1,  width=10, height=5,
                    bg='white', command=lambda: self.buttonClick(4))
    self.button4.grid(row=1, column=0, padx=5, pady=5)

    self.button5 = tk.Button(master= self.frame1,  width=10, height=5,
                    bg='white', command=lambda: self.buttonClick(5))
    self.button5.grid(row=1, column=1, padx=5, pady=5)

    self.button6 = tk.Button(master=self.frame1,  width=10, height=5,
                    bg='white', command=lambda: self.buttonClick(6))
    self.button6.grid(row=1, column=2, padx=5, pady=5)

    self.button7 = tk.Button(master=self.frame1,  width=10, height=5,
                             bg='white', command=lambda: self.buttonClick(7))
    self.button7.grid(row=2, column=0, padx=5, pady=5)

    self.button8 = tk.Button(master=self.frame1,  width=10, height=5,
                             bg='white', command=lambda:  self.buttonClick(8))
    self.button8.grid(row=2, column=1, padx=5, pady=5)

    self.button9 = tk.Button(master=self.frame1,  width=10, height=5,
                             bg='white', command=lambda:  self.buttonClick(9))
    self.button9.grid(row=2, column=2, padx=5, pady=5)

    self.restartFrame = tk.Frame(master = master, border = 2)
    self.restartFrame.pack()

    self.restartButton = tk.Button(master = self.restartFrame,text = "Restart",state=tk.DISABLED, width=10,height=3,command=lambda:self.restart())
    self.restartButton.grid(row =0,column=1,padx=10,pady=10)

  def buttonClick(self,x):
    if(x==1):
      

      row,col = 0,0
      if(self.game.moveCount%2!=0):
        self.button1["text"] = self.game.player1.symbol
      else:
        self.button1["text"] = self.game.player2.symbol
      self.game.moveCount += 1
      self.game.playGame(row,col)
      

    if(x==2):
     
      row,col = 0,1
      if (self.game.moveCount % 2 != 0):
        self.button2["text"] = self.game.player1.symbol
      else:
        self.button2["text"] = self.game.player2.symbol
      self.game.moveCount += 1
      self.game.playGame(row,col)
      

    if (x == 3):
     
      row,col = 0,2
      if (self.game.moveCount % 2 != 0):
        self.button3["text"] = self.game.player1.symbol
      else:
        self.button3["text"] = self.game.player2.symbol
      self.game.moveCount += 1
      self.game.playGame(row,col)
      

    if (x == 4):
      
      row, col = 1, 0
      if (self.game.moveCount % 2 != 0):
        self.button4["text"] = self.game.player1.symbol
      else:
        self.button4["text"] = self.game.player2.symbol
      self.game.moveCount += 1
      self.game.playGame(row, col)
      

    if (x == 5):
      
      row, col = 1, 1
      if (self.game.moveCount % 2 != 0):
        self.button5["text"] = self.game.player1.symbol
      else:
        self.button5["text"] = self.game.player2.symbol
      self.game.moveCount += 1
      self.game.playGame(row, col)
      

    if (x == 6):
      
      row, col = 1, 2
      if (self.game.moveCount % 2 != 0):
        self.button6["text"] = self.game.player1.symbol
      else:
        self.button6["text"] = self.game.player2.symbol
      self.game.moveCount += 1
      self.game.playGame(row, col)
      

    if (x == 7):
    
      row, col = 2, 0
      if (self.game.moveCount % 2 != 0):
        self.button7["text"] = self.game.player1.symbol
      else:
        self.button7["text"] = self.game.player2.symbol
      self.game.moveCount += 1
      self.game.playGame(row, col)
      

    if (x == 8):
   
      row, col = 2, 1
      if (self.game.moveCount % 2 != 0):
        self.button8["text"] = self.game.player1.symbol
      else:
        self.button8["text"] = self.game.player2.symbol
      self.game.moveCount += 1
      self.game.playGame(row, col)
      

    if (x == 9):
      
      row, col = 2, 2
      if (self.game.moveCount % 2 != 0):
        self.button9["text"] = self.game.player1.symbol
      else:
        self.button9["text"] = self.game.player2.symbol
      self.game.moveCount += 1
      self.game.playGame(row, col)
     
    
    if(self.game.winner == True and not self.game.draw):
      self.disableButtons()
      print(self.game.moveCount)
      if(self.game.moveCount %2 ==0):
        tkinter.messagebox.showinfo("Tic Tac Toe", "Player one wins")
        self.restartButton["state"] = tk.NORMAL
      else:
        tkinter.messagebox.showinfo("Tic Tac Toe", "Player two wins")
        self.restartButton["state"] = tk.NORMAL

    if(self.game.draw == True):
      self.disableButtons()
      tkinter.messagebox.showinfo("Tic Tac Toe", "Draw")
      self.restartButton["state"] = tk.NORMAL


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
  
  def restart(self):
    self.game.board.clearBoard()
    self.game.winner = False
    self.game.draw = False
    self.game.moveCount = 1
    self.restartButton["state"]= tk.DISABLED

    self.button1["text"] = " "
    self.button2["text"] = " "
    self.button3["text"] = " "
    self.button4["text"] = " "
    self.button5["text"] = " "
    self.button6["text"] = " "
    self.button7["text"] = " "
    self.button8["text"] = " "
    self.button9["text"] = " "


    self.button1["state"] = tk.NORMAL
    self.button2["state"] = tk.NORMAL
    self.button3["state"] = tk.NORMAL
    self.button4["state"] = tk.NORMAL
    self.button5["state"] = tk.NORMAL
    self.button6["state"] = tk.NORMAL
    self.button7["state"] = tk.NORMAL
    self.button8["state"] = tk.NORMAL
    self.button9["state"] = tk.NORMAL

    
    
    
      
        










