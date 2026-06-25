# Radiobutton

import tkinter as tk

root=tk.Tk()
root.geometry("600x400")

var = tk.StringVar()

tk.Radiobutton(root,text="Male",variable=var,value="Male").pack()
tk.Radiobutton(root,text="Female",variable=var,value="Female").pack()

root.mainloop()
