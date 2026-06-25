#3)place(): is a geometry manager used to position widgets at specific x and y coordinates. 

import tkinter as tk
root = tk.Tk()
root.geometry("600x400")
btn = tk.Button(root, text = "Clicke Me")
btn.place(x=250,y=200)
root.mainloop()
