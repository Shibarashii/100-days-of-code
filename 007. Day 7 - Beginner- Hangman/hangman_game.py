import random
import hangman_art
import hangman_words

stages = hangman_art.stages
word_list = hangman_words.word_list
logo = hangman_art.logo

chosen_word = random.choice(word_list)
display = []
for letter in chosen_word:
    display.append("_")

display_word = "".join(display)
mistakes = 0

print(logo)
print("Save him by guessing letters correctly to form the word.")
print(stages[mistakes])

while chosen_word != display_word and mistakes != 6:
    print("\n" + display_word)

    guess = input("Guess a letter: ").lower()

    correct_letter = False
    for i in range(len(chosen_word)):
        if guess == display[i]:
            print("Letter already guessed.")
            correct_letter = True
            print(stages[mistakes])
            break
        elif chosen_word[i] == guess:
            display[i] = chosen_word[i]
            display_word = "".join(display)
            correct_letter = True
            print(f"{chosen_word[i]} is a correct guess! ")
            print(stages[mistakes])

    if not correct_letter:
        mistakes += 1
        if mistakes != 6:
            print(f"A mistake! It will cost him his life. Remaining life: {6 - mistakes}")
            print(stages[mistakes])


if chosen_word == display_word:
    print("\nYou saved him.")
    print(stages[mistakes])
else:
    print(f"\nThe word was {chosen_word}")
    print("You didn't manage to save him.")
    print(stages[mistakes])
