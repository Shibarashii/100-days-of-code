print("Welcome to the tip calculator")

total = float(input("What was the total bill? $"))
people_count = float(input("How many people to split the bill? "))
percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))

split = total / people_count
payment_of_each_person = split + (split * percentage / 100)

print(f"Each person should pay: {payment_of_each_person:.2f}")
