"""
Number Guessing Game
---------------------
The computer picks a random number in a given range.
The player has a limited number of attempts to guess it,
receiving "Too High" / "Too Low" hints along the way.
"""

import random


def get_guess(prompt, low, high):
    """Keep asking until the user enters a valid integer within range."""
    while True:
        value = input(prompt).strip()
        try:
            guess = int(value)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        if guess < low or guess > high:
            print(f"Please enter a number between {low} and {high}.")
            continue

        return guess


def choose_difficulty():
    print("\nChoose a difficulty level:")
    print("1. Easy   (1-50,  10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard   (1-200, 5 attempts)")

    levels = {
        "1": (1, 50, 10),
        "2": (1, 100, 7),
        "3": (1, 200, 5),
    }

    while True:
        choice = input("Enter choice (1-3): ").strip()
        if choice in levels:
            return levels[choice]
        print("Invalid choice. Please select 1, 2, or 3.")


def play_round():
    low, high, max_attempts = choose_difficulty()
    secret_number = random.randint(low, high)
    attempts_used = 0

    print(f"\nI'm thinking of a number between {low} and {high}.")
    print(f"You have {max_attempts} attempts. Good luck!\n")

    while attempts_used < max_attempts:
        remaining = max_attempts - attempts_used
        guess = get_guess(f"Attempt {attempts_used + 1}/{max_attempts} - Your guess: ", low, high)
        attempts_used += 1

        if guess == secret_number:
            print(f"\n🎉 Correct! The number was {secret_number}.")
            print(f"You guessed it in {attempts_used} attempt(s).")
            return
        elif guess < secret_number:
            print("Too Low!\n")
        else:
            print("Too High!\n")

        remaining_after = max_attempts - attempts_used
        if remaining_after > 0:
            print(f"({remaining_after} attempt(s) left)")

    print(f"\n💀 Out of attempts! The number was {secret_number}.")


def main():
    print("===== Number Guessing Game =====")

    while True:
        play_round()
        again = input("\nDo you want to play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
