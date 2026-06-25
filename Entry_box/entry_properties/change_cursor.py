#cursor: change the cursore icon

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
    bd=2,cursor="hand2")
entry.pack()
root.mainloop()
