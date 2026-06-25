#icursor:
#The icursor() method is used to move the insertion cursor
#(text cursor) to a specific position inside an Entry widget.
#index = position where you want to place the cursor.
#Index starts from 0.
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
entry.icursor(2)
entry.focus()
entry.pack()
root.mainloop()
