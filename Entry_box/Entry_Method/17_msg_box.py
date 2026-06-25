#Message Box

import tkinter as tk
from tkinter import messagebox

def show_info():
    messagebox.showinfo("info","hello razin!")

root=tk.Tk()
root.geometry("600x400")

btn = tk.Button(root,text="Show Message", command=show_info)
btn.pack()

root.mainloop()
