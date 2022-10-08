from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizzInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(bg=THEME_COLOR, padx=20, pady=20)
        # configure canvas
        self.canvas = Canvas(bg="white", width=300, height=250)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)
        self.question = self.canvas.create_text(150, 125, justify="center", font=("Arial", 20, "italic"),
                                                text="Here goes the text", fill=THEME_COLOR, width=290)
        # buttons configuration
        self.true_img = PhotoImage(file="./images/true.png")
        self.false_img = PhotoImage(file="./images/false.png")
        self.true_button = Button(image=self.true_img, highlightthickness=0)
        self.false_button = Button(image=self.false_img, highlightthickness=0)
        self.true_button.grid(column=0, row=2, padx=20, pady=20)
        self.false_button.grid(column=1, row=2, padx=20, pady=20)
        # score tag
        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0, padx=20, pady=20)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfigure(self.question, text=q_text)