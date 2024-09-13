from game_data import data
from model import SocialMediaPlatform
import random

vs_art = """
        _    __    
        | |  / /____
        | | / / ___/
        | |/ (__  ) 
        |___/____(_)
"""


def format_person(person: SocialMediaPlatform) -> str:
    """Format the SocialMediaPlatform data into a presentable string"""
    return f"{person.name}, a {person.description}, from {person.country}"


def game():
    platforms = [SocialMediaPlatform(**item) for item in data]

    score = 0
    game_should_continue = True
    person_b = platforms.pop(random.randint(0, len(platforms) - 1))  # 随机选择并移除

    while game_should_continue and len(platforms) > 0:
        person_a = person_b
        person_b = platforms.pop(
            random.randint(0, len(platforms) - 1)
        )  # 再次随机选择并移除

        print(f"Compare A: {format_person(person_a)}")
        print(vs_art)
        print(f"Against B: {format_person(person_b)}")

        # Ask the user to make a guess
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Check if the user is correct
        a_follower_count = person_a.follower_count
        b_follower_count = person_b.follower_count
        is_correct = (guess == "a" and a_follower_count > b_follower_count) or (
            guess == "b" and b_follower_count > a_follower_count
        )

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

    if len(platforms) == 0:
        print("No more platforms to compare. Game over!")


# Entry point of the script, calls the main function to start the Car Rental System
if __name__ == "__main__":
    game()
