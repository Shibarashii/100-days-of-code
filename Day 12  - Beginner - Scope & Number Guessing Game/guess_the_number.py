import random

HARD_LEVEL_ATTEMPTS = 5
EASY_LEVEL_ATTEMPTS = 10


def ask_replay():
    play_again = input(f"Play again? Type 'yes' to play again and 'no' if not: ")
    return play_again.lower() == "yes"


def play_game():
    print("Welcome to the Number Guessing Game! ")
    print("I'm thinking of a number between 1 and 100")

    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty not in ["easy", "hard"]:
            print("Please choose a valid difficulty.")
            continue

        if difficulty == "easy":
            attempts = EASY_LEVEL_ATTEMPTS
        else:
            attempts = HARD_LEVEL_ATTEMPTS

        random_number = random.randint(1, 100)
        while attempts > 0:
            print(f"You have {attempts} attempts remaining to guess the number")
            try:
                guess = int(input("Make a guess: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if guess == random_number:
                print(f"You won! The number is {random_number}")
                break
            elif guess > random_number:
                print("Too high.\nGuess again.")
            else:
                print("Too low.\nGuess again.")

            attempts -= 1

        if attempts == 0:
            print(f"\nYou lost. The number was {random_number}")

        if not ask_replay():
            break


play_game()
