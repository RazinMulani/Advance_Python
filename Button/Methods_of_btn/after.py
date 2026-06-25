#8) after(): is used to execute a function after a specified amount of time.

import tkinter as tk
root = tk.Tk()
root.geometry("600x400")
def greet():
    print("hello")
    
btn = tk.Button(root, text = "Clicke Me",command=greet)
btn.after(3000,lambda:btn.config(text="Done"))
btn.pack()
root.mainloop()
