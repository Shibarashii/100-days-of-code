from pathlib import Path

root = Path(__file__).parent

# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

input_path = root / "Input"
letters_path = input_path / "Letters"
names_path = input_path / "Names"
output_path = root / "Output" / "ReadyToSend"


# Read names
with open(names_path / "invited_names.txt", "r") as names_file:
    names = names_file.readlines()

# Read letter
with open(letters_path / "starting_letter.txt", "r") as letter_file:
    content = letter_file.read()

# Output
placeholder = "[name]"
for name in names:
    stripped_name = name.strip()
    new_content = content.replace(placeholder, stripped_name)
    with open(output_path / f"letter_for_{stripped_name}.txt", "w") as new_letter:
        new_letter.write(new_content)
