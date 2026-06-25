#9) update(): forces Tkinter to process all pending events and immediately refresh the GUI.

import tkinter as tk
root = tk.Tk()
root.geometry("600x400")
def greet():
    print("hello")

btn = tk.Button(root, text = "Clicke Me",command=greet)
btn.pack()
btn.update()
print("Referesh The System")
root.mainloop()
