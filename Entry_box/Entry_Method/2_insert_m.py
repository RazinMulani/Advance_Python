# Insert: insert the value , the value show in text box
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
entry.insert(0,"Hello User!")
entry.pack()
root.mainloop()
