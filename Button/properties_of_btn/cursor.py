#Cursor : if u hover the mouse on the button that time change the mouse cursor

import tkinter as tk
root = tk.Tk()
root.geometry("600x400")
btn = tk.Button(root, text = "Hello",cursor = "hand2")
btn.pack()
root.mainloop()
