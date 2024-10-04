import tkinter as tk

def show_input_text():
    # Get the text from the Entry widget and update the label
    input_text = entry.get()
    label.config(text=input_text, font=("Courier", 20, "bold"))

window = tk.Tk()
window.minsize(width=400,height=400)
window.title("Welcome to my window.")

# Create an Entry widget for text input
entry = tk.Entry(window)
entry.pack()

# Create a button to trigger the display of input text
button = tk.Button(window, text="Show Text", command=show_input_text)
button.pack()

# Create a label to display the input text
label = tk.Label(window, text="Your text will appear here")
label.pack()

window.mainloop()