# Button: How to add btn in window
import tkinter as tk

def hello():
    print("Button Clicked")

root= tk.Tk()
root.geometry("600x400")

btn = tk.Button(root,text="me",command =hello)
btn.pack()

root.mainloop()
