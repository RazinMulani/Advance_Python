# State: The state option controls whether a widget can be used, edited, or interacted with.
#normal: User can be intract, disable: user can not be interact, readonly: user read the content only but dont use btn

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
    bd=2,state="disable")
entry.pack()
root.mainloop()
