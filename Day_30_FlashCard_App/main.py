from tkinter import *
import pandas as pd
from random import choice
BACKGROUND_COLOR = "#B1DDC6"

timer = None


# ---------------------------- CHANGE CARD ------------------------------- #
def change_card():
    global current
    current = choice(french_words_list)
    # language = next(iter(current))
    # word = current[language]
    word = current["French"]
    canvas.itemconfig(canvas_iamge, image=card_image_front)
    canvas.itemconfig(Language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=f"{word}", fill="black")
    count_down(3)

# ---------------------------- READ CSV ------------------------------- #
french_words = pd.read_csv("data/french_words.csv")
french_words_list = french_words.to_dict(orient="records")

# ---------------------------- TIMER ------------------------------- #

def count_down(count):
    global current
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)

    elif count == 0:
        word = current["English"]
        canvas.itemconfig(canvas_iamge, image=card_image_back)
        canvas.itemconfig(Language_text, text="English", fill="white")
        canvas.itemconfig(word_text, text=f"{word}", fill="white")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

current = choice(french_words_list)
# language = next(iter(current))
# word = current[language]
word = current["French"]

# Flash Card Image
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_image_front = PhotoImage(file="images/card_front.png")
card_image_back = PhotoImage(file="images/card_back.png")
# To make logo be in center of canvas (half the coordinates in canvas)
canvas_iamge = canvas.create_image(400, 263, image=card_image_front)

# Card Text
Language_text = canvas.create_text(400, 150, text="French", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text=f"{word}", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


# Button
wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=change_card)
wrong_button.grid(column=0, row=1)
tick_button_image = PhotoImage(file="images/right.png")
tick_button = Button(image=tick_button_image, highlightthickness=0, command=change_card)
tick_button.grid(column=1, row=1)

count_down(3)

window.mainloop()
