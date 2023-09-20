import random
from tkinter import *
from tkinter import messagebox
import pandas


BACKGROUND_COLOR = "#B1DDC6"

try:
    words_data = pandas.read_csv("./data/words_to_learn.csv")

except (FileNotFoundError, pandas.errors.EmptyDataError):
    original_data = pandas.read_csv("data/all_words.csv")
    to_learn = original_data.to_dict(orient="records")

else:
    to_learn = words_data.to_dict(orient="records")


current_card = {}


def next_card():
    global current_card, flip_timer, to_learn
    window.after_cancel(flip_timer)

    try:
        current_card = random.choice(to_learn)
    except IndexError:
        messagebox.showinfo(title="Warning", message="List of words is empty now.\nThe list will be restored!")
        to_learn = pandas.read_csv("data/all_words.csv").to_dict(orient="records")
        next_card()

    else:
        canvas.itemconfig(canvas_background, image=CARD_FRONT_IMG)
        canvas.itemconfig(language_text, text="French", fill="black")
        canvas.itemconfig(word, text=current_card["French"], fill="black")

    # After rendering french card flip_card() is called
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_background, image=CARD_BACK_IMG)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")


def known_word():
    global words_data

    try:
        to_learn.remove(current_card)
    except ValueError:
        pass
    else:
        pandas.DataFrame(to_learn).to_csv("./data/words_to_learn.csv", index=False)

    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# When program launches function flip card is called after 3000ms, but we disable it by calling next_card() function
# on the bottom of the file
flip_timer = window.after(3000, flip_card)


RIGHT_IMG = PhotoImage(file="./images/right.gif")
WRONG_IMG = PhotoImage(file="./images/wrong.gif")
CARD_BACK_IMG = PhotoImage(file="./images/card_back.gif")
CARD_FRONT_IMG = PhotoImage(file="./images/card_front.gif")

canvas = Canvas(width=400, height=263, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_background = canvas.create_image(200, 131)
language_text = canvas.create_text(200, 200, font=("Ariel", 40, "italic"))
word = canvas.create_text(200, 100, font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_button = Button(image=WRONG_IMG, bd=0, highlightbackground=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(column=0, row=1)

right_button = Button(image=RIGHT_IMG, bd=0, highlightbackground=BACKGROUND_COLOR, command=known_word)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()
