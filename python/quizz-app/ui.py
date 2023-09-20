from tkinter import *
from quiz_brain import QuizBrain  # QuizBrain class import in order to get all the functions, etc.

THEME_COLOR = "#375362"


class QuizInterface:

    # Without defining a data type this file will not know what is a data type of input.
    # It also makes sure that code does not contain any errors when initializing the class in other file.
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        right_img = PhotoImage(file="./images/right.gif")
        wrong_img = PhotoImage(file="./images/wrong.gif")

        self.score_label = Label(text="SCORE: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.quiz_text = self.canvas.create_text(150, 125, width=275, fill=THEME_COLOR, font=("Arial", 20, "italic"))

        self.right_button = Button(image=right_img, bd=0, command=self.right_button_pressed)
        self.right_button.grid(column=0, row=2)

        self.wrong_button = Button(image=wrong_img, bd=0, command=self.wrong_button_pressed)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"SCORE: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            # Changing color of label to THEME_COLOR in order to get rid of the bug with gray background
            # self.score_label.config(fg=THEME_COLOR)
            self.canvas.itemconfig(self.quiz_text, text=q_text)
            self.buttons_enabled()
        else:
            self.canvas.itemconfig(self.quiz_text, text="You've reached the end of the quiz!!!")
            self.buttons_disabled()

    def right_button_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        self.buttons_disabled()

    def wrong_button_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        self.buttons_disabled()

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def buttons_enabled(self):
        self.right_button.config(state="normal")
        self.wrong_button.config(state="normal")

    def buttons_disabled(self):
        self.right_button.config(state="disabled")
        self.wrong_button.config(state="disabled")
