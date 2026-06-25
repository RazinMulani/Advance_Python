#ListBox

import tkinter as tk

root=tk.Tk()
root.geometry("600x400")

listBox = tk.Listbox(root)

listBox.insert(1,"Python")
listBox.insert(2,"JAVA")
listBox.insert(3,"C")
listBox.insert(4,"C++")

listBox.pack()

root.mainloop()
