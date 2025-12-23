from secret_auction_art import logo


bid_values = {}

print(logo)
print("Welcome to the secret auction program. ")

while True:
    name = input("What is your name? ")
    bid = float(input("What's your bid?: $"))

    bid_values[name] = bid

    while True:
        more_bidder = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
        if more_bidder in ["yes", "no"]:
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

    if more_bidder == "no":
        break


highest_bid = 0.00
highest_bidder = ""
for bidder in bid_values:
    value = bid_values[bidder]
    if value > highest_bid:
        highest_bid = value
        highest_bidder = bidder

print(f"The highest bidder is {highest_bidder} with a bid of ${highest_bid}")