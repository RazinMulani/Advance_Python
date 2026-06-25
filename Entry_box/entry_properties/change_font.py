# Change Font of Inside the Entry box text

import tkinter as tk

root = tk.Tk()
root.geometry("600x400")

entry = tk.Entry(root,width = 30, font=("Arial",20,"bold"))
entry.pack()

root.mainloop()
