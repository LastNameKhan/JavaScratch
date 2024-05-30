from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random

random_index = random.randint(0,12)

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

# question_bank = Question(question_data[random_index]["text"], question_data[random_index]["answer"])
# print(question_data[random_index]["text"], question_data[random_index]["answer"])