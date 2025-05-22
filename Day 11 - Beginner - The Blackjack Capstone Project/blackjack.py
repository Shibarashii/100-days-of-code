# ############## Blackjack Project #####################
#
# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.
#
# ############## Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.


from blackjack_art import logo
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

dealer_cards = []
player_cards = []


def random_card():
    """Returns a random card."""
    return random.choice(cards)


def initiate_cards():
    """Initiate the cards."""
    dealer_cards.append(random_card())
    dealer_cards.append(random_card())

    player_cards.append(random_card())
    player_cards.append(random_card())


def check_score(hand):
    """Check the score of a hand."""
    total = sum(hand)
    ace_count = hand.count(11)

    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1

    return total


def show_cards(revealed=False):
    """Show or reveal the cards."""
    if not revealed:
        print(f"\nYour cards: {player_cards}, current score: {check_score(player_cards)}")
        print(f"Dealer's first card: {dealer_cards[0]}")

    if revealed:
        print(f"\nYour final cards: {player_cards}. Final Score: {check_score(player_cards)}")
        print(f"Dealer's final cards: {dealer_cards}. Final Score: {check_score(dealer_cards)}")


def play_again():
    """Asks the player if they want to play again."""
    choice = input("Type 'y' to play again, type 'n' to exit: ")
    if choice == "y":
        dealer_cards.clear()
        player_cards.clear()
        print("")
        return True
    elif choice == "n":
        return False


def compare_cards():
    """Reveals the cards and compares the final scores."""
    print("\n\n------------- Final Scores -------------")
    show_cards(True)
    dealer_total = check_score(dealer_cards)
    player_total = check_score(player_cards)
    if dealer_total < player_total <= 21:
        print("You have higher cards. You won!")
    elif player_total < dealer_total <= 21:
        print("You have lower cards. You lost.")
    elif player_total > 21:
        print("You went over 21. You lost.")
    elif dealer_total > 21:
        print("Dealer went over 21. You won!")
    else:
        print("It's a draw")


def gameplay():
    """Plays the Blackjack Game."""
    print(logo)

    initiate_cards()
    show_cards()

    dealer_total = check_score(dealer_cards)
    player_total = check_score(player_cards)
    game_over = False

    if dealer_total == 21:
        print("\nThe dealer has Blackjack, you lost")
        show_cards(True)
        if play_again():
            gameplay()

    elif player_total > 21:
        print("\nYour cards went over 21, you lost")
        show_cards(True)
        if play_again():
            gameplay()

    while not game_over:
        choice = input("Type 'y' to get another card, type 'n' to pass: ")
        if choice == "y":
            player_cards.append(random_card())
            player_total = check_score(player_cards)
            show_cards()
            if player_total > 21:
                compare_cards()
                if play_again():
                    gameplay()
                return
            continue

        elif choice == "n":
            while dealer_total < 16:
                dealer_cards.append(random_card())
                dealer_total = check_score(dealer_cards)

            compare_cards()
            if play_again():
                gameplay()
            return


gameplay()

