#Entry Index Values
#Index	Meaning
#0	First Character
#1	Second Character
#2	Third Character
#tk.END	Last Character
# Example:

import tkinter as tk
root=tk.Tk()
root.geometry("600x400")

entry = tk.Entry(root,width = 30)
entry.insert(0,"Python")# insert the value
entry.delete(0,3)# Delete first 3 values (0,3-1)
entry.pack() # op: hon
root.mainloop()
