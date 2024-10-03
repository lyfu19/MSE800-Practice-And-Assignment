import tkinter as tk

class CurrencyConverter:
    def __init__(self, window):
        self.window = window
        window.minsize(width=300,height=150)
        self.window.title("Currency Converter")

        # Create label for instruction
        self.label = tk.Label(window, text="Enter amount and select currencies:")
        self.label.pack()

        # Create entry for input amount
        self.amount_entry = tk.Entry(window)
        self.amount_entry.pack()

        # Create labels for currency selection
        self.from_label = tk.Label(window, text="From Currency:")
        self.from_label.pack()

        self.from_currency = tk.StringVar(window)
        self.from_currency.set("NZD")  # Default value

        self.from_menu = tk.OptionMenu(window, self.from_currency, "USD", "EUR", "CNY", "NZD")
        self.from_menu.pack()

        self.to_label = tk.Label(window, text="To Currency:")
        self.to_label.pack()

        self.to_currency = tk.StringVar(window)
        self.to_currency.set("CNY")  # Default value

        self.to_menu = tk.OptionMenu(window, self.to_currency, "USD", "EUR", "CNY", "NZD")
        self.to_menu.pack()

        # Create button to perform conversion
        self.convert_button = tk.Button(window, text="Convert", command=self.convert)
        self.convert_button.pack()

        # Create label to show result
        self.result_label = tk.Label(window, text="")
        self.result_label.pack()

    def convert(self):
        amount = float(self.amount_entry.get())
        from_curr = self.from_currency.get()
        to_curr = self.to_currency.get()

        # Define conversion rates for USD, EUR, CNY, and NZD
        rates = {
            "USD": {"USD": 1, "EUR": 0.91, "CNY": 7.02, "NZD": 1.60},
            "EUR": {"USD": 1.10, "EUR": 1, "CNY": 7.75, "NZD": 1.77},
            "CNY": {"USD": 0.14, "EUR": 0.13, "CNY": 1, "NZD": 0.23},
            "NZD": {"USD": 0.62, "EUR": 0.57, "CNY": 4.38, "NZD": 1}
        }

        converted_amount = amount * rates[from_curr][to_curr]
        self.result_label.config(text=f"Converted Amount: {converted_amount:.2f} {to_curr}")

# Create the window
window = tk.Tk()

# Create an instance of the converter
app = CurrencyConverter(window)

# Run the window's main loop
window.mainloop()