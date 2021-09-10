from tkinter import *
import pandas as pd
from random import choice
BACKGROUND_COLOR = "#B1DDC6"

timer = None


# ---------------------------- CHANGE CARD ------------------------------- #
def change_card():
    global current_card, flip_timer
    # Cancel the function call to flip card if user change card before the english word is revealed
    window.after_cancel(flip_timer)
    current_card = choice(french_words_list)
    canvas.itemconfig(canvas_iamge, image=card_image_front)
    canvas.itemconfig(Language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    flip_timer = window.after(3000,flip_card)


def is_known():
    french_words_list.remove(current_card)
    french_words_to_learn = pd.DataFrame(french_words_list)
    french_words_to_learn.to_csv("data/words_to_learn.csv", index=False)
    change_card()

# ---------------------------- READ CSV ------------------------------- #
try:
    # retrieve saved progress
    french_words = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    # fetch new 
    french_words = pd.read_csv("data/french_words.csv")
finally:
     french_words_list = french_words.to_dict(orient="records")

# ---------------------------- FLIP CARD ------------------------------- #

def flip_card():
    global current_card

    canvas.itemconfig(canvas_iamge, image=card_image_back)
    canvas.itemconfig(Language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

current_card = choice(french_words_list)

flip_timer = window.after(3000,flip_card)

# Flash Card Image
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_image_front = PhotoImage(file="images/card_front.png")
card_image_back = PhotoImage(file="images/card_back.png")
# To make logo be in center of canvas (half the coordinates in canvas)
canvas_iamge = canvas.create_image(400, 263, image=card_image_front)

# Card Text
Language_text = canvas.create_text(400, 150, text="French", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text=current_card["French"], fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


# Button
wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=change_card)
wrong_button.grid(column=0, row=1)
tick_button_image = PhotoImage(file="images/right.png")
tick_button = Button(image=tick_button_image, highlightthickness=0, command=is_known)
tick_button.grid(column=1, row=1)

window.mainloop()
