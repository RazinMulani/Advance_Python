#Combobox

import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.geometry("600x400")

combo = ttk.Combobox(root)
combo['values']=("Python","Java","C","C++")
combo.pack()

root.mainloop()
