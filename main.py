from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from bs4 import BeautifulSoup
from ui import QuizzInterface

questions = [Question(q_text=BeautifulSoup(question["question"], "html.parser"), q_answer=question["correct_answer"])
             for question in question_data]
quiz = QuizBrain(questions)
quiz_ui = QuizzInterface(quiz)
