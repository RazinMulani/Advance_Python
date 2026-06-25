#5)cget(): is used to get (retrieve) the current value of a widget's property.

import tkinter as tk
root = tk.Tk()
root.geometry("600x400")
btn = tk.Button(root, text = "Clicke Me")
btn.pack()
print(btn.cget("text"))
root.mainloop()
