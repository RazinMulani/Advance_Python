# Import Tk Inter and perform title, geomatry, minsize, maxsize, resizable

import tkinter as tk # tkinter library used to create GUI application in python
root = tk.Tk() # root is the parent window where all widget will be placed
#widget means button,labels, entires etc.

root.title("Import The TKinter") # Set the window title

root.geometry("600x400")   # initial size of window

root.configure(bg="lightblue")# background color window

root.minsize(400,200)   # minimum size of window
root.maxsize(1200,800)  # maximum size of window

root.resizable(True,True) # allow the user to resize the window

root.mainloop()# start the event loop using mainloop() to keep the application running
