from tkinter import *

THEME_COLOR = "#375362"


class QuizzInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(bg=THEME_COLOR, padx=20, pady=20)
        # configure canvas
        self.canvas = Canvas(bg="white", width=300, height=250)
        self.canvas.grid(column=0, row=1, columnspan=2)
        self.question = self.canvas.create_text(150, 125, justify="center", font=("Arial", 20, "italic"),
                                                text="Here goes the text")
        # buttons configuration
        self.true_img = PhotoImage(file="./images/true.png")
        self.false_img = PhotoImage(file="./images/false.png")
        self.true_button = Button(image=self.true_img)
        self.false_button = Button(image=self.false_img)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)
        # score tag
        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0)
        self.window.mainloop()
