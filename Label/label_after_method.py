# Q1)Create a Tkinter label and update its text to 'Who' after 3 seconds using after().

import tkinter as tk
root = tk.Tk()

root.title("Change The value in a secande")
root.geometry("600x500")
root.configure(bg="mint cream")

lbel = tk.Label(root,text="Nok Nok!",bg="skyblue",fg="white",font=("Arial",20,"bold"),height = 3,
                width = 18)

#after(): Schedules a task to run later.3000 mileseconds = 3 seconds
lbel.after(3000,lambda:lbel.config(text="Who")) # connfig() modifies the properties of the label
lbel.after(6000,lambda:lbel.config(text="I'm Your Future"))
lbel.after(9000,lambda:lbel.config(text="Wait What!"))
lbel.pack()
# cget()=configuration gate
# it is used to get(read)the current widget's property

print(lbel.cget("text"))

root.mainloop()
