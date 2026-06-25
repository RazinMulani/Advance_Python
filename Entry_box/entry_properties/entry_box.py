#Create Entry box(tk.Enter())

import tkinter as tk

root = tk.Tk()
root.geometry("600x400")

entry = tk.Entry(root)# create one entry box
entry.pack()

root.mainloop()
