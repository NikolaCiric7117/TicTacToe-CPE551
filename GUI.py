
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
                             height=5, bg='white', command=lambda:  self.buttonclick(1))


    self.button1.grid(row=0, column=0, padx=5, pady=5)

    self.button2 = tk.Button(master=self.frame1, text='', width=10, height=5,
                             bg='white', command=lambda:  self.buttonclick(2))
    self.button2.grid(row=0, column=1, padx=5, pady=5)

    self.button3 = tk.Button(master= self.frame1, text='', width=10, height=5,
                             bg='white', command=lambda:  self.buttonclick(3))
    self.button3.grid(row=0, column=2, padx=5, pady=5)

    self.button4 = tk.Button(master= self.frame1, text='', width=10, height=5,
                    bg='white', command=lambda: buttonclick(4))
    self.button4.grid(row=1, column=0, padx=5, pady=5)

    self.button5 = tk.Button(master= self.frame1, text='', width=10, height=5,
                    bg='white', command=lambda: buttonclick(5))
    self.button5.grid(row=1, column=1, padx=5, pady=5)

    self.button6 = tk.Button(master=self.frame1, text='', width=10, height=5,
                    bg='white', command=lambda: buttonclick(6))
    self.button6.grid(row=1, column=2, padx=5, pady=5)

    self.button7 = tk.Button(master=self.frame1, text='', width=10, height=5,
                             bg='white', command=lambda: self.buttonclick(7))
    self.button7.grid(row=2, column=0, padx=5, pady=5)

    self.button8 = tk.Button(master=self.frame1, text='', width=10, height=5,
                             bg='white', command=lambda:  self.buttonclick(8))
    self.button8.grid(row=2, column=1, padx=5, pady=5)

    self.button9 = tk.Button(master=self.frame1, text='', width=10, height=5,
                             bg='white', command=lambda:  self.buttonclick(9))
    self.button9.grid(row=2, column=2, padx=5, pady=5)

  def buttonclick(self,x):
    print("hello")



root = tk.Tk()
gui = Gui(root)
gui.master.mainloop()






