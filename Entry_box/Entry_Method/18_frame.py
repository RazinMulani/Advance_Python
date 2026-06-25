# Frame

import tkinter as tk
root = tk.Tk()
root.geometry("400x300")

frame = tk.Frame(root,bd=2,relief="solid",width=200,height=100)
frame.pack()

tk.Label(frame,text="Inside Frame").pack()
root.mainloop()
