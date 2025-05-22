import random

rock = '''
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


rps = [rock, paper, scissors]

cpu_choice = random.randint(0, len(rps) - 1)

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors \n"))

print(f"You chose: \n\n {rps[choice]} \n")
print(f"Computer chose: \n\n {rps[cpu_choice]} \n")

if cpu_choice == choice:
    result = "Draw"

elif choice == 0:  # Rock
    if cpu_choice == 1:
        result = "Lose"
    else:
        result = "Win"

elif choice == 1:  # Paper
    if cpu_choice == 2:
        result = "Lose"
    else:
        result = "Win"

else:
    if cpu_choice == 0:
        result = "Lose"
    else:
        result = "Win"

print(f"Result: {result}")
