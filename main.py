from GUI import *
#main function which runs the entire Tic Tac Toe game with GUI implementation
def main():

  #initalizes root to a new TK object 
  root = tk.Tk()

  #initlaizes gui to a new GUI object
  gui = Gui(root)

  #built in TK function that infinitely loops which displays and runs the tic tac toe game
  gui.master.mainloop()
  
#runns the main function
if __name__=="__main__":
    main()
