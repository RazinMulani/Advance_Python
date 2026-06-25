# Entry method:
# get()

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
def active_btn():
    name = entry.get()
    print(name)

btn=tk.Button(root,text="Enter",command=active_btn)
btn.pack()
root.mainloop()
