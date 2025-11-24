from pathlib import Path
from tkinter import *
import pandas as pd
import random

root = Path(__file__).parent
img_path = root / "images"
data_path = root / "data"

german_words_path = data_path / "german_words.csv"
card_back_path = img_path / "card_back.png"
card_front_path = img_path / "card_front.png"
right_path = img_path / "right.png"
wrong_path = img_path / "wrong.png"

BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

flip_timer = None
generated_words = set()
current_word = {}
correct_answers = set()
to_learn = None

try:
    to_learn = pd.read_csv(
        data_path/"words_to_learn.csv").to_dict(orient="records")
    print("Loaded words_to_learn.csv")
except FileNotFoundError:
    to_learn = pd.read_csv(
        data_path/"german_words.csv").to_dict(orient="records")
    print("Loaded german_words.csv")


def check_button():
    to_learn.remove(current_word)
    generate_word()
    to_save = pd.DataFrame(to_learn)
    to_save.to_csv(data_path/"words_to_learn.csv", index=False)
    print(len(to_learn))


def generate_word():
    global current_word, flip_timer

    window.after_cancel(flip_timer)
    current_word = random.choice(to_learn)
    canvas.itemconfig(canvas_img, image=card_front_img)
    canvas.itemconfig(word_text, text=current_word["German"], fill="black")
    canvas.itemconfig(title_text, text="German", fill="black")
    flip_timer = window.after(3000, flip)


def flip():
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(word_text, text=current_word["English"], fill="white")
    canvas.itemconfig(title_text, text="English", fill="white")


# ------------------------------- UI -------------------------------
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip)
canvas = Canvas(width=800, height=526,
                bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


card_front_img = PhotoImage(file=card_front_path)
card_back_img = PhotoImage(file=card_back_path)
canvas_img = canvas.create_image(400, 263, image=card_front_img)

title_text = canvas.create_text(
    400, 150, text="German", fill="black", font=LANG_FONT)
word_text = canvas.create_text(
    400, 263, text="Word", fill="black", font=WORD_FONT)

x_button_img = PhotoImage(file=wrong_path)
x_button = Button(image=x_button_img, highlightthickness=0,
                  command=generate_word)
x_button.grid(row=1, column=0)

check_button_img = PhotoImage(file=right_path)
check_button = Button(image=check_button_img,
                      highlightthickness=0, command=check_button)
check_button.grid(row=1, column=1)
generate_word()

window.mainloop()
