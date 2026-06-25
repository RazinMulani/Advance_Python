# Increase width of Entry Box or Text Box
# not "HEIGHT" is not support in entry box
import tkinter as tk

root = tk.Tk()
root.geometry("600x400")

entry = tk.Entry(root, width = 50)
entry.pack()

root.mainloop()
