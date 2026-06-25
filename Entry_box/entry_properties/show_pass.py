# Show: Use for creating a password field

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
entry.pack()
passw = tk.Entry(root,show="*",width=30,
    bg="lightyellow",
    fg="blue",
    relief="solid",
    bd=2,
    font=("Arial",20,'bold'))
passw.pack()
root.mainloop()
