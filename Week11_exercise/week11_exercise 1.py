import tkinter as tk
# from tkinter import *

window = tk.Tk()
window.minsize(width=400,height=400)
window.title("Welcome to my window.")

# Create a label
label = tk.Label(window, text="This is the original text")
label.pack()

def change_label_text():
    label.config(text="Text has been changed!", font=("Courier", 20, "bold"))

# Create a button
button = tk.Button(window, text="Change Text", command=change_label_text)
button.pack()

window.mainloop()