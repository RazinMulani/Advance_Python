# Get Text From Entry:

import tkinter as tk

def show_text():
    print(entry.get())
    
root=tk.Tk()
root.geometry("600x400")

entry = tk.Entry(root)
entry.pack()

btn = tk.Button(root,text = "show",command=show_text)
btn.pack()

root.mainloop()5
