from datetime import datetime

def say_good_morning():
    print("Good morning neighbour")

def dec_name(func):
    def wrapper():
        current_hour = datetime.now().hour
        if 6 <= current_hour < 12:
            func()  # Only run the function if it's between 6 AM and 12 PM
        else:
            print("This function can only be executed in the morning (6 AM to 12 PM).")
    return wrapper

# Applying the decorator
say_good_morning = dec_name(say_good_morning)

# Call the function to test
say_good_morning()