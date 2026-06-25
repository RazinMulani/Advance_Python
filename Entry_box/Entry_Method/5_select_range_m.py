# select_range:Select The Range

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
    bd=2)
entry.insert(0,"Hello!")
entry.focus()
entry.select_range(0,tk.END)
entry.pack()
root.mainloop()
