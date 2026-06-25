#Ceate image in Button

import tkinter as tk
from tkinter import PhotoImage
root = tk.Tk()
root.geometry("600x400")
img = PhotoImage(file = "logo.png")
btn = tk.Button(root,image=img,relief="solid",bd=2)
btn.pack()
root.mainloop()
