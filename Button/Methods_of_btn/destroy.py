#7) Destroy(): is used to permanently remove a widget or close a window.

import tkinter as tk
root = tk.Tk()
root.geometry("600x400")
def greet():
    print("hello")
    
btn = tk.Button(root, text = "Clicke Me",command=greet)
btn.pack()

btn.destroy()
print("Destroy the btn")
root.mainloop()
