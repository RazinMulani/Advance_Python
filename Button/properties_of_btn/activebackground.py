#activebackground: This option is used to change bg color of a button whenn the useer click or press it

import tkinter as tk
root = tk.Tk()
root.geometry("600x400")
btn = tk.Button(root, text = "Change The Background Color",activebackground="red")
btn.pack()
root.mainloop()
