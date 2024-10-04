import tkinter as tk

class DistanceConverter:
    def __init__(self, window):
        self.window = window
        window.minsize(width=200,height=150)
        self.window.title("Distance converter")

        # Label to display instructions
        self.label = tk.Label(window, text="Enter distance in miles:")
        self.label.pack()

        # Entry widget to input miles
        self.entry = tk.Entry(window)
        self.entry.pack()

        # Button to perform conversion
        self.convert_button = tk.Button(window, text="Convert to Km", command=self.convert_to_km)
        self.convert_button.pack()

        # Label to display the result
        self.result_label = tk.Label(window, text="Result will be shown here.")
        self.result_label.pack()

    def convert_to_km(self):
        try:
            # Get the input from the Entry widget, convert it to float, and calculate kilometers
            miles = float(self.entry.get())
            km = miles * 1.60934
            # Display the result in the result_label
            self.result_label.config(text=f"{miles} miles is {km:.2f} kilometers")
        except ValueError:
            # Handle invalid input (non-numeric)
            self.result_label.config(text="Please enter a valid number")

# Create the main window and start the application
window = tk.Tk()
app = DistanceConverter(window)
window.mainloop()