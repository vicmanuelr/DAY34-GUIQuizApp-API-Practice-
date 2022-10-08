class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

# TODO 3: check if we're at the end of the quiz
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

# TODO 1: ask the user per questions
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q.{self.question_number}: {current_question.text}"
        # user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        # self.check_answer(user_answer, current_question.answer)

# TODO 2: check if the answer was correct
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}.\n")
