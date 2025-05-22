from caesar_cipher_art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(plaint_text, shift_amount, cipher_direction):
    cipher_text = ""
    for char in plaint_text:
        if alphabet.count(char) == 0:
            cipher_text += char
            continue

        if cipher_direction == "encode":
            if alphabet.index(char) + shift_amount > 25:
                new_index = alphabet.index(char) + shift_amount % 26
            else:
                new_index = alphabet.index(char) + shift_amount

            cipher_text += alphabet[new_index]

        elif cipher_direction == "decode":
            if alphabet.index(char) - shift_amount < 0:
                new_index = alphabet.index(char) - shift_amount % 26
            else:
                new_index = alphabet.index(char) - shift_amount

            cipher_text += alphabet[new_index]

    print(cipher_text)


print(logo)

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt (or 'exit' to quit):\n").lower()

    if direction not in ['encode', 'decode']:
        print("Please enter a valid option.")
        continue

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)

    restart = input("Do you want to continue? Type 'Yes' or 'No'. ")
    if restart == 'No':
        break
