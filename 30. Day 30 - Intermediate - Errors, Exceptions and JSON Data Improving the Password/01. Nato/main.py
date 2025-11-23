import pandas
from pathlib import Path

csv_path = Path(__file__).parent / "nato_phonetic_alphabet.csv"
data = pandas.read_csv(csv_path)

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def genenate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError as e:
        print("Sorry, only letters in the alphabet")
        genenate_phonetic()
    else:
        print(output_list)


genenate_phonetic()
