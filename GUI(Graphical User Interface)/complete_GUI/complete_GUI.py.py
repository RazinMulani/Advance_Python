# Advanced Python

'''
import tkinter as tk
root = tk.Tk()
root.title("My First Window")
root.geometry("400x300")
root.resizable(True,True)
root.configure(bg="lightblue")
root.iconbitmap("palmtree.ico")
#root.state("zoomed")
#root.attributes("-fullscreen",True)
#root.minsize(400,300)
#root.maxsize(1200,800)
#root.withdraw()
#root.deiconify()
#root.quit()
#root.update()
#root.after(3000,root.destroy)
#print(root.winfo_width())
#print(root.winfo_height())
#print(root.winfo_screenwidth())
#print(root.winfo_screenheight())
def on_close():
    print("Window Closing")

root.protocol("WM_DELETE_WINDOW", on_close)


#root.destroy()
root.mainloop()

# Window Properties
'''

# Example Of Import Tkinter 
'''
import tkinter as tk

root = tk.Tk()

root.title("Tkinter Demo")
root.geometry("600x400")
root.configure(bg="lightyellow")

root.minsize(400,200)
root.maxsize(1200,800)

root.resizable(True,True)
root.mainloop()
'''

# Add a Lable
'''
import tkinter as tk

root = tk.Tk()
root.title("Lable Example")
root.geometry("600x400")

root.configure(bg="lightyellow")

lbel =  tk.Label(root,text="Welcome To TKinter!",bg="yellow",fg="blue",font=("Arial",30,"bold"),
                 width=18, height=2)
lbel.config(text="First Text")
lbel.config(bg="black")
#lbel.grid(row=1,column=10)
#lbel.place(x=100,y=50)

#add another label for chacking

lbel1 =  tk.Label(root,text="Welcome To TKinter!",bg="blue",fg="blue",font=("Arial",30,"bold"),
                 width=18, height=2)
lbel1.config(text="Second Text")
lbel1.config(bg="red")
lbel1.grid(row=2,column=5)
lbel.place(x=100,y=50)

#lbel.after(3000,lambda:lbel.config(text="changed"))
lbel.update()
print("refresh")
lbel.pack()
#lbel.destroy()
#print(lbel.cget("text"))
root.mainloop()

'''
# Border Styles (relief)
'''
import tkinter as tk
root = tk.Tk()
root.title("Add Border")
root.geometry("600x400")

lbl = tk.Label(root,text = "Solid", relief="solid", bd = 3)
lbl.grid(row=1,column=1)

lbl1 = tk.Label(root,text = "Flat", relief="flat", bd = 3)
lbl1.grid(row=1,column=2)

lbl3 = tk.Label(root,text = "Raised", relief="raised", bd = 3)
lbl3.grid(row=1,column=3)

lbl4 = tk.Label(root,text = "Ridge", relief="ridge", bd = 3)
lbl4.grid(row=1,column=4)

lbl5 = tk.Label(root,text = "Groove", relief="groove", bd = 3)
lbl5.grid(row=1,column=5)

#lbl.pack()

root.mainloop()

'''
'''
# Image Label
import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk()  # Create window first

img = PhotoImage(file="logo.png")

lbl = tk.Label(root, image=img,relief=("solid"),bd=3)
lbl.pack()

root.mainloop()
'''
# Add a Button
'''
import tkinter as tk

def hello():
    print("Button Clicked")

root= tk.Tk()
root.geometry("600x400")
# I perform most of the widget at a time like " bg for background","FG for change text olor","height for
# give the height for the button", "width for give the width of the button","font for u are change the font
# style using a font widget"
btn = tk.Button(root,text="me",command =hello,height=3,width=18,fg="white",bg="gray",font=("Arial",20,"bold"))
btn.pack()

root.mainloop()

# text widget: it is used to give the value of button or write the insteraction like clicke me, butn etc.
# command widget: use for calling function

'''
# relief (Use the Border)
'''
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
'''
#activebackground: This option is used to change bg color of a button whenn the useer click or press it
'''
import tkinter as tk
root = tk.Tk()
root.geometry("600x400")
btn = tk.Button(root, text = "Change The Background Color",activebackground="red")
btn.pack()
root.mainloop()
'''
#activeforeground:This option is used to change the text color of a button when the user click or press it
'''
import tkinter as tk
root = tk.Tk()
root.geometry("600x400")
btn = tk.Button(root, text = "Change The Background Color",activeforeground="red")
btn.pack()
root.mainloop()
'''
#Ceate image in Button
'''
import tkinter as tk
from tkinter import PhotoImage
root = tk.Tk()
root.geometry("600x400")
img = PhotoImage(file = "logo.png")
btn = tk.Button(root,image=img,relief="solid",bd=2)
btn.pack()
root.mainloop()
'''

#Cursor : if u hover the mouse on the button that time change the mouse cursor
'''
import tkinter as tk
root = tk.Tk()
root.geometry("600x400")
btn = tk.Button(root, text = "Hello",cursor = "hand2")
btn.pack()
root.mainloop()
'''

# button Method
#1) pack()
'''
import tkinter as tk
root = tk.Tk()
root.geometry("600x400")
btn = tk.Button(root, text = "Clicke Me")
btn.pack()# this method place a widgae inside the tkinter window and makes it visible

root.mainloop()
'''
#2) grid(): is a geometry manager used to arrange widgets in rows and columns.
'''
import tkinter as tk
root = tk.Tk()
root.geometry("600x400")
btn = tk.Button(root, text = "Clicke Me")
btn.grid(row=1,column = 1)
#btn.pack()
root.mainloop()
'''
#3)place(): is a geometry manager used to position widgets at specific x and y coordinates. 
'''
import tkinter as tk
root = tk.Tk()
root.geometry("600x400")
btn = tk.Button(root, text = "Clicke Me")
btn.place(x=250,y=200)
root.mainloop()
'''

#4)config(): is used to change the properties of a widget after it has been created.
'''
import tkinter as tk
root = tk.Tk()
root.geometry("600x400")
btn = tk.Button(root, text = "Clicke Me")
btn.config(text="BTN")
btn.pack()
root.mainloop()
'''
#5)cget(): is used to get (retrieve) the current value of a widget's property.
'''
import tkinter as tk
root = tk.Tk()
root.geometry("600x400")
btn = tk.Button(root, text = "Clicke Me")
btn.pack()
print(btn.cget("text"))
root.mainloop()
'''
#6) invoke(): is used to execute a button's command programmatically, as if the user had clicked the button.

'''
import tkinter as tk
root = tk.Tk()
root.geometry("600x400")
def greet():
    print("hello")
    
btn = tk.Button(root, text = "Clicke Me",command=greet)
btn.pack()

btn.invoke()
root.mainloop()
'''
#7) Destroy(): is used to permanently remove a widget or close a window.
'''
import tkinter as tk
root = tk.Tk()
root.geometry("600x400")
def greet():
    print("hello")
    
btn = tk.Button(root, text = "Clicke Me",command=greet)
btn.pack()

btn.destroy()
print("Destroy the btn")
root.mainloop()
'''
#8) after(): is used to execute a function after a specified amount of time.
'''
import tkinter as tk
root = tk.Tk()
root.geometry("600x400")
def greet():
    print("hello")
    
btn = tk.Button(root, text = "Clicke Me",command=greet)
btn.after(3000,lambda:btn.config(text="Done"))
btn.pack()
root.mainloop()
'''
#9) update(): forces Tkinter to process all pending events and immediately refresh the GUI.
'''
import tkinter as tk
root = tk.Tk()
root.geometry("600x400")
def greet():
    print("hello")

btn = tk.Button(root, text = "Clicke Me",command=greet)
btn.pack()
btn.update()
print("Referesh The System")
root.mainloop()
'''

#Example:
'''
import tkinter as tk

def hello():
    lbl.config(text="Button Clicked")

root = tk.Tk()
root.geometry("300x200")

lbl = tk.Label(root, text="Welcome")
lbl.pack(pady=10)

btn = tk.Button(
    root,
    text="Click Me",
    bg="lightblue",
    fg="black",
    font=("Arial", 12, "bold"),
    command=hello
)

btn.pack()

root.mainloop()
'''
# Step 4: Add an Entry Box
'''
import tkinter as tk

root = tk.Tk()
root.geometry("600x400")

entry = tk.Entry(root)
entry.pack()

root.mainloop()
'''

# width
'''
import tkinter as tk

root = tk.Tk()
root.geometry("600x400")

entry = tk.Entry(root, width = 50)
entry.pack()

root.mainloop()
'''

# font
'''
import tkinter as tk

root = tk.Tk()
root.geometry("600x400")

entry = tk.Entry(root,width = 30, font=("Arial",20,"bold"))
entry.pack()

root.mainloop()
'''

# bg = change the background color
'''
import tkinter as tk

root = tk.Tk()
root.geometry("600x400")

entry = tk.Entry(root,width = 30, font=("Arial",20,"bold"), bg="lightyellow")
entry.pack()

root.mainloop()
'''

# FG = change the text color
'''
import tkinter as tk

root = tk.Tk()
root.geometry("600x400")
entry = tk.Entry(root,width = 30, font=("Arial",20,"bold"), bg="lightyellow", fg = "blue")
entry.pack()
root.mainloop()

'''
# relief and bd= Add border for text box
'''
import tkinter as tk

root = tk.Tk()
root.geometry("600x400")
entry = tk.Entry(
    root,
    width=30,
    font=("Arial",20,'bold'),
    bg="lightyellow",
    fg="blue",
    relief="solid",
    bd=2)
entry.pack()
root.mainloop()
'''
# Justify Content: arrange text so that align evenly on the left, center, right, and both side
#note justify content by default is left position
'''
import tkinter as tk

root = tk.Tk()
root.geometry("600x400")
entry = tk.Entry(
    root,
    width=30,
    font=("Arial",20,'bold'),
    bg="lightyellow",
    fg="blue",
    relief="solid",
    bd=2,
    justify="center")# -->right --> left(bydefault)

entry.pack()
root.mainloop()
'''
# Show: Use for creating a password field
'''
import tkinter as tk

root = tk.Tk()
root.geometry("600x400")
entry = tk.Entry(
    root,
    width=30,
    font=("Arial",20,'bold'),
    bg="lightyellow",
    fg="blue",
    relief="solid",
    bd=2)
entry.pack()
passw = tk.Entry(root,show="*",width=30,
    bg="lightyellow",
    fg="blue",
    relief="solid",
    bd=2,
    font=("Arial",20,'bold'))
passw.pack()
root.mainloop()
'''
# State: The state option controls whether a widget can be used, edited, or interacted with.
#normal: User can be intract, disable: user can not be interact, readonly: user read the content only but dont use btn
'''
import tkinter as tk

root = tk.Tk()
root.geometry("600x400")
entry = tk.Entry(
    root,
    width=30,
    font=("Arial",20,'bold'),
    bg="lightyellow",
    fg="blue",
    relief="solid",
    bd=2,state="disable")
entry.pack()
root.mainloop()
'''
#cursor: change the cursore icon
'''
import tkinter as tk

root = tk.Tk()
root.geometry("600x400")
entry = tk.Entry(
    root,
    width=30,
    font=("Arial",20,'bold'),
    bg="lightyellow",
    fg="blue",
    relief="solid",
    bd=2,cursor="hand2")
entry.pack()
root.mainloop()
'''

# Entry method:
# get()
'''
import tkinter as tk

root = tk.Tk()
root.geometry("600x400")
entry = tk.Entry(
    root,
    width=30,
    font=("Arial",20,'bold'),
    bg="lightyellow",
    fg="blue",
    relief="solid",
    bd=2)
entry.pack()
def active_btn():
    name = entry.get()
    print(name)

btn=tk.Button(root,text="Enter",command=active_btn)
btn.pack()
root.mainloop()
'''
# Insert: insert the value , the value show in text box
'''
import tkinter as tk

root = tk.Tk()
root.geometry("600x400")
entry = tk.Entry(
    root,
    width=30,
    font=("Arial",20,'bold'),
    bg="lightyellow",
    fg="blue",
    relief="solid",
    bd=2)
entry.insert(0,"Hello User!")
entry.pack()
root.mainloop()
'''
# Delete
'''
import tkinter as tk

root = tk.Tk()
root.geometry("600x400")
entry = tk.Entry(
    root,
    width=30,
    font=("Arial",20,'bold'),
    bg="lightyellow",
    fg="blue",
    relief="solid",
    bd=2)
entry.insert(0,"Hello User!")
entry.delete(0,tk.END)
entry.pack()
root.mainloop()
'''
# Delete only one charachter
'''
import tkinter as tk
root = tk.Tk()
root.geometry("600x400")
entry = tk.Entry(
    root,
    width=30,
    font=("Arial",20,'bold'),
    bg="lightyellow",
    fg="blue",
    relief="solid",
    bd=2)
entry.insert(0,"Hello User!")
entry.delete(0)
entry.pack()
root.mainloop()
'''
# Focus: Focuse courser to Entry Box
'''
import tkinter as tk
root = tk.Tk()
root.geometry("600x400")
entry = tk.Entry(
    root,
    width=30,
    font=("Arial",20,'bold'),
    bg="lightyellow",
    fg="blue",
    relief="solid",
    bd=2)
entry.focus()
entry.pack()
root.mainloop()
'''
# select_range:Select The Range
'''
import tkinter as tk
root = tk.Tk()
root.geometry("600x400")
entry = tk.Entry(
    root,
    width=30,
    font=("Arial",20,'bold'),
    bg="lightyellow",
    fg="blue",
    relief="solid",
    bd=2)
entry.insert(0,"Hello!")
entry.focus()
entry.select_range(0,tk.END)
entry.pack()
root.mainloop()
'''
#icursor:
'''
import tkinter as tk
root = tk.Tk()
root.geometry("600x400")
entry = tk.Entry(
    root,
    width=30,
    font=("Arial",20,'bold'),
    bg="lightyellow",
    fg="blue",
    relief="solid",
    bd=2)
entry.insert(0,"Hello!")
entry.icursor(2)
entry.focus()
entry.pack()
root.mainloop()
'''
# Config: Change the value of property
'''
import tkinter as tk
root = tk.Tk()
root.geometry("600x400")
entry = tk.Entry(
    root,
    width=30,
    font=("Arial",20,'bold'),
    bg="lightyellow",
    fg="blue",
    relief="solid",
    bd=2)
entry.insert(0,"Hello!")
entry.config(bg="black")
entry.config(fg="white")
entry.pack()
root.mainloop()
'''
# cget(): Read the property value
'''
import tkinter as tk
root = tk.Tk()
root.geometry("600x400")
entry = tk.Entry(
    root,
    width=30,
    font=("Arial",20,'bold'),
    bg="lightyellow",
    fg="blue",
    relief="solid",
    bd=2)
entry.insert(0,"Hello!")
entry.pack()
print(entry.cget("width"))
print(entry.cget("font"))
print(entry.cget("bg"))
print(entry.cget("fg"))
print(entry.cget("relief"))
print(entry.cget("bd"))
root.mainloop()
'''
# destroy(): remove the text box
'''
import tkinter as tk
root = tk.Tk()
root.geometry("600x400")
entry = tk.Entry(
    root,
    width=30,
    font=("Arial",20,'bold'),
    bg="lightyellow",
    fg="blue",
    relief="solid",
    bd=2)
entry.insert(0,"Hello!")
entry.select_range(0,tk.END)
entry.pack()
entry.destroy()
print("Remove the Text Box In The Field")
root.mainloop()
'''

# Practical Example:
'''
import tkinter as tk

def show():
    print(entry.get())

root = tk.Tk()
root.geometry("300x200")

entry = tk.Entry(root, width=25)
entry.pack(pady=10)

entry.insert(0, "Enter Name")
entry.focus()
entry.select_range(0,tk.END)

btn = tk.Button(root,text="Show",command=show)
btn.pack()

root.mainloop()
'''
#Entry Index Values
#Index	Meaning
#0	First Character
#1	Second Character
#2	Third Character
#tk.END	Last Character
# Example:
'''
import tkinter as tk
root=tk.Tk()
root.geometry("600x400")

entry = tk.Entry(root,width = 30)
entry.insert(0,"Python")# insert the value
entry.delete(0,3)# Delete first 3 values (0,3-1)
entry.pack() # op: hon
root.mainloop()
'''
# mini login form(practice again)
'''
import tkinter as tk
from tkinter import messagebox

def login():
    username = user_entry.get()
    password = pass_entry.get()

    messagebox.showinfo(
        "Login",
        f"Username: {username}\nPassword: {password}"
    )

root = tk.Tk()
root.title("Login Form")
root.geometry("300x200")

tk.Label(root, text="Username").pack()

user_entry = tk.Entry(root)
user_entry.pack()

tk.Label(root, text="Password").pack()

pass_entry = tk.Entry(root, show="*")
pass_entry.pack()

btn = tk.Button(root,text="Login",command=login)
btn.pack(pady=10)

root.mainloop()
'''
# Get Text From Entry:
'''
import tkinter as tk

def show_text():
    print(entry.get())
    
root=tk.Tk()
root.geometry("600x400")

entry = tk.Entry(root)
entry.pack()

btn = tk.Button(root,text = "show",command=show_text)
btn.pack()

root.mainloop()5

'''
# Chec Button(checkbox)
'''
import tkinter as tk

root=tk.Tk()
root.geometry("600x400")

var = tk.IntVar()

check = tk.Checkbutton(root,text="Python",variable=var)
check.pack()

root.mainloop()
'''
# Radiobutton
'''
import tkinter as tk

root=tk.Tk()
root.geometry("600x400")

var = tk.StringVar()

tk.Radiobutton(root,text="Male",variable=var,value="Male").pack()
tk.Radiobutton(root,text="Female",variable=var,value="Female").pack()

root.mainloop()
'''
#ListBox
'''
import tkinter as tk

root=tk.Tk()
root.geometry("600x400")

listBox = tk.Listbox(root)

listBox.insert(1,"Python")
listBox.insert(2,"JAVA")
listBox.insert(3,"C")
listBox.insert(4,"C++")

listBox.pack()

root.mainloop()
'''
#Combobox
'''
import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.geometry("600x400")

combo = ttk.Combobox(root)
combo['values']=("Python","Java","C","C++")
combo.pack()

root.mainloop()
'''
#Message Box
'''
import tkinter as tk
from tkinter import messagebox

def show_info():
    messagebox.showinfo("info","hello razin!")

root=tk.Tk()
root.geometry("600x400")

btn = tk.Button(root,text="Show Message", command=show_info)
btn.pack()

root.mainloop()
'''
# Frame

import tkinter as tk
root = tk.Tk()
root.geometry("400x300")

frame = tk.Frame(root,bd=2,relief="solid",width=200,height=100)
frame.pack()

tk.Label(frame,text="Inside Frame").pack()
root.mainloop()








