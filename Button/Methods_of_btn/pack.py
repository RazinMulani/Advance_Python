#1) pack()

import tkinter as tk
root = tk.Tk()
root.geometry("600x400")
btn = tk.Button(root, text = "Clicke Me")
btn.pack()# this method place a widgae inside the tkinter window and makes it visible

root.mainloop()
