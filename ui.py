from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizzInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(bg=THEME_COLOR, padx=20, pady=20)
        self.timer = None
        # configure canvas
        self.canvas = Canvas(bg="white", width=300, height=250)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)
        self.question = self.canvas.create_text(150, 125, justify="center", font=("Arial", 20, "italic"),
                                                text="Here goes the text", fill=THEME_COLOR, width=290)
        # buttons configuration
        self.true_img = PhotoImage(file="./images/true.png")
        self.false_img = PhotoImage(file="./images/false.png")
        self.true_button = Button(image=self.true_img, highlightthickness=0, command=self.true_answer)
        self.false_button = Button(image=self.false_img, highlightthickness=0, command=self.false_answer)
        self.true_button.grid(column=0, row=2, padx=20, pady=20)
        self.false_button.grid(column=1, row=2, padx=20, pady=20)
        # score tag
        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0, padx=20, pady=20)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.true_button.config(state="active")
        self.false_button.config(state="active")
        self.canvas.configure(background="white")
        if self.quiz.still_has_questions():
            if self.timer is not None:
                self.window.after_cancel(self.timer)
            q_text = self.quiz.next_question()
            self.canvas.itemconfigure(self.question, text=q_text)
        else:
            self.game_end()

    def true_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_answer(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(background="green")
            self.score.configure(text=f"Score: {self.quiz.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.timer = self.window.after(1000, func=self.get_next_question)
        else:
            self.canvas.configure(background="red")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.timer = self.window.after(1000, func=self.get_next_question)

    def game_end(self):
        self.canvas.itemconfigure(self.question, text=f"You've completed the quiz."
                                                      f"\nYour final score is: "
                                                      f"{self.quiz.score}/{self.quiz.question_number}")
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
