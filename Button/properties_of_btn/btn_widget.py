# Add some weidget like " bg for background","FG for change text olor","height for
# give the height for the button", "width for give the width of the button","font for u are change the font
# style using a font widget"

import tkinter as tk

def hello():
    print("Button Clicked")

root= tk.Tk()
root.geometry("600x400")
btn = tk.Button(root,text="me",command =hello,height=3,width=18,fg="white",bg="gray",
                font=("Arial",20,"bold"))
btn.pack()

root.mainloop()
