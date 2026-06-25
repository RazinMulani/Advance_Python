#6) invoke(): is used to execute a button's command programmatically, as if the user had clicked the button.

import tkinter as tk
root = tk.Tk()
root.geometry("600x400")
def greet():
    print("hello")
    
btn = tk.Button(root, text = "Clicke Me",command=greet)
btn.pack()

btn.invoke()
root.mainloop()
