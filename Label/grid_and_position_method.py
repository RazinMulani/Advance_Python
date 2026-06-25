#Q) Create a Tkinter program with two labels.Position them using row and column in the Grid layout and
#make the GUI look creative.

import tkinter as tk
root = tk.Tk()

root.title("Use Grid Method and Position Method")
root.geometry("600x400")

root.configure(bg="mint cream")
#1st use grid method and 3rd one use place method
# Label 1
lbl = tk.Label(root,text="First Label Box",bg="gold",fg="blue",font=("Arial",20,"bold"),
               height=3,width=18)
lbl.grid(row = 1,column =1)
#lbl.pack()
lbl_2 = tk.Label(root,text="Second Label Box",bg="maroon",fg="white",font=("Arial",20,"bold"),
                 height=3,width=18)
lbl_2.grid(row = 1, column = 2)
#lbl_2.pack()

# Add One More and place to the next of secand label box
lbl_3 = tk.Label(root,text="3rd Label Box",bg="gray",fg="white",font=("Arial",20,"bold"),
                 height=3,width=18)
lbl_3.place(x=600,y=0)
#lbl_3.pack()
root.mainloop()

