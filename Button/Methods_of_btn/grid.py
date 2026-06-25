#2) grid(): is a geometry manager used to arrange widgets in rows and columns.

import tkinter as tk
root = tk.Tk()
root.geometry("600x400")
btn = tk.Button(root, text = "Clicke Me")
btn.grid(row=1,column = 1)
#btn.pack()
root.mainloop()
