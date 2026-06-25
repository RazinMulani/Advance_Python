#4)config(): is used to change the properties of a widget after it has been created.

import tkinter as tk
root = tk.Tk()
root.geometry("600x400")
btn = tk.Button(root, text = "Clicke Me")
btn.config(text="BTN")
btn.pack()
root.mainloop()
