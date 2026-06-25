# Practical Example:

import tkinter as tk

def show():
    print(entry.get())

root = tk.Tk()
root.geometry("300x200")

entry = tk.Entry(root, width=25)
entry.pack(pady=10)

entry.insert(0, "Enter Name")
entry.focus()
entry.select_range(0,tk.END)

btn = tk.Button(root,text="Show",command=show)
btn.pack()

root.mainloop()
