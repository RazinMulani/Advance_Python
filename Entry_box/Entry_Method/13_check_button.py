# Chec Button(checkbox)

import tkinter as tk

root=tk.Tk()
root.geometry("600x400")

var = tk.IntVar()

check = tk.Checkbutton(root,text="Python",variable=var)
check.pack()

root.mainloop()
