# Justify Content: arrange text so that align evenly on the left, center, right, and both side
#note justify content by default is left position

import tkinter as tk

root = tk.Tk()
root.geometry("600x400")
entry = tk.Entry(
    root,
    width=30,
    font=("Arial",20,'bold'),
    bg="lightyellow",
    fg="blue",
    relief="solid",
    bd=2,
    justify="center")# -->right --> left(bydefault)

entry.pack()
root.mainloop()
