import tkinter as tk
# from tkinter import *

window = tk.Tk()
window.minsize(width=400,height=400)
window.title("My first window.")
label = tk.Label(text="this is my first label")
label.pack()

def button_clicked():
    print("the button is clicked")

button = tk.Button(text="Click Me", command=button_clicked)
button.pack()


window.mainloop()