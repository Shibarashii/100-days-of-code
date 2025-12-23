import pandas as pd
from pathlib import Path

root = Path(__file__).parent
csv_path = root / "nato_phonetic_alphabet.csv"

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

phonetic_df = pd.read_csv(csv_path)

phonetic_dict = {row["letter"]: row["code"]
                 for (index, row) in phonetic_df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter word: ").upper()
name_to_phonetic = [phonetic_dict[letter] for letter in word]

print(name_to_phonetic)
