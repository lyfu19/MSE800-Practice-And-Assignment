def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(f"the result is {n}")

calculate(n=2, add=2, multiply=4)