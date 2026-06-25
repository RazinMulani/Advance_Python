#activeforeground:This option is used to change the text color of a button when the user click or press it
'''
import tkinter as tk
root = tk.Tk()
root.geometry("600x400")
btn = tk.Button(root, text = "Change The Background Color",activeforeground="red")
btn.pack()
root.mainloop()
