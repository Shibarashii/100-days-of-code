import random
from higher_lower_game_art import logo, vs
from higher_lower_game_data import data


print(logo)


def is_correct(answer):
    if answer == "A":
        if person_a['follower_count'] > person_b['follower_count']:
            return True
        else:
            return False
    elif answer == "B":
        if person_b['follower_count'] > person_a['follower_count']:
            return True
        else:
            return False


def generate_random_person():
    return random.choice(data)


score = 0

game_over = False
while not game_over:
    person_a = generate_random_person()
    person_b = generate_random_person()

    while person_b == person_a:
        person_b = generate_random_person()

    print(f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}")
    print(vs)
    print(f"Compare B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}")
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    if is_correct(choice):
        score += 1
        print(f"\nYou're right!. Current score: {score}")
        continue

    else:
        print(f"\nSorry, that's wrong. Final score: {score}")
        game_over = True





