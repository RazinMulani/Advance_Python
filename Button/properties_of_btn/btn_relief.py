# relief (Use the Border)

import tkinter as tk
root= tk.Tk()
root.title("Create Btn Using A Border properties or relief properties")
root.geometry("600x400")

def click_btn():
    print("Hello World!")
btn = tk.Button(root, text = "Click Me",command=click_btn, relief="solid",bd=2)
# u have so many choices in the relief like flat, raised, sunken, groove, ridge, solid
btn.pack()
root.mainloop()
