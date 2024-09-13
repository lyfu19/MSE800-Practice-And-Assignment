import random
from game_data import data # type: ignore

def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(guess, A_followers, B_followers):
    if A_followers > B_followers:
        return guess == "a"
    else:
        return guess == "b"

def play_game():
    print("Welcome to the Higher or Lower Game!")
    score = 0
    game_should_continue = True
    account_B = random.choice(data)  # Initialize the second account

    # Game loop
    while game_should_continue:
        # Make account_A the previous account_B and choose a new account_B
        account_A = account_B
        account_B = random.choice(data)
        
        while account_A == account_B:
            account_B = random.choice(data)

        print(f"Compare A: {format_data(account_A)}.")
        print("VS")
        print(f"Against B: {format_data(account_B)}.")

        # Ask for user input
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  
        A_followers = account_A["follower_count"]
        B_followers = account_B["follower_count"]
        is_correct = check_answer(guess, A_followers, B_followers)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}.")

# Main loop to restart the game if the user wants
while True:
    play_game()
    replay = input("Do you want to play again? Type 'y' for yes or 'n' for no: ").lower()
    if replay != 'y':
        print("Thank you for playing!")
        break