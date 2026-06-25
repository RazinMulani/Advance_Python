# cget(): Read the property value

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
entry.pack()
print(entry.cget("width"))
print(entry.cget("font"))
print(entry.cget("bg"))
print(entry.cget("fg"))
print(entry.cget("relief"))
print(entry.cget("bd"))
root.mainloop()
