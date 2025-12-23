import random
from pathlib import Path
from tkinter import *
from tkinter import messagebox
import pyperclip

root = Path(__file__).parent
img_path = root / "logo.png"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_random_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    random_password = []

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    random_password += ([random.choice(letters) for _ in range(nr_letters)])
    random_password += ([random.choice(symbols) for _ in range(nr_symbols)])
    random_password += ([random.choice(numbers) for _ in range(nr_numbers)])
    random.shuffle(random_password)
    random_password = "".join(random_password)
    pyperclip.copy(random_password)

    password_entry.insert(0, random_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website == "" or email == "" or password == "":
        messagebox.showerror(message="Please fill up the form")
    else:
        is_ok = messagebox.askokcancel(
            title="website", message=f"Save details?\nEmail: {email}\nPassword: {password}")
        if is_ok and website is not None and password is not None:
            with open(f"{root/'data.txt'}", "a") as f:
                f.write(f"{website} | {email} | {password}\n")

        website_entry.delete(0, END)
        password_entry.delete(0, END)

    # ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
pw_img = PhotoImage(file=img_path)

canvas.create_image(100, 100, image=pw_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

# Entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "shiba@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_btn = Button(
    text="Generate Password", command=generate_random_password)
generate_password_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
