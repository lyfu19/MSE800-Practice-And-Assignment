from art import text2art

logo = text2art("Black Jack")
print(logo)

import random

# Use this list as the deck of cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """Returns a random card from the deck."""
    return random.choice(cards)

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards."""
    # Check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # This is a blackjack
    
    # Check for an 11 (ace). If the score is over 21, remove the 11 and replace it with a 1.
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(user_score, computer_score):
    """Compares the user and computer scores and declares the winner."""
    if user_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "Computer has a blackjack! You lose."
    elif user_score == 0:
        return "You have a blackjack! You win!"
    elif user_score > 21:
        return "You went over 21! You lose."
    elif computer_score > 21:
        return "Computer went over 21! You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    """The main game logic for Blackjack."""
    print("Welcome to the game of Blackjack!")

    # Deal the user and computer 2 cards each
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]
    
    game_over = False

    while not game_over:
        # Calculate the score for both the user and computer
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        
        # Check if the game is over (either by blackjack or by going over 21)
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            # Ask the user if they want to draw another card
            should_continue = input("Type 'y' to get another card, type 'n' to pass: ")
            if should_continue == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    # Once the user is done, let the computer play
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# Ask the user if they want to restart the game.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()