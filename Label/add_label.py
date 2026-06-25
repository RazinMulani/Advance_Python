# Add A Label

import tkinter as tk
root = tk.Tk()

root.title("Add A Label")

root.geometry("600x400")

root.configure(bg="lavender")

# Add Label and try some properties(BG = background, FG=Change the figure color, Font= Change font size
#fon stylle etc,Height= change height , Width=change width)

lbel = tk.Label(root,text="Welcome To TKinter",bg="red",fg="white",height = 3,width=18,font=("solid",20,"bold"))
lbel.pack()
root.mainloop()

