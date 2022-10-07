from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from bs4 import BeautifulSoup

questions = [Question(q_text=BeautifulSoup(question["question"], "html.parser"), q_answer=question["correct_answer"])
             for question in question_data]
quiz = QuizBrain(questions)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz.\nYour final score is: {quiz.score}/{quiz.question_number}")
