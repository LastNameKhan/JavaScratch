class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


new_question = Question("Hello", "False")
print(new_question.text)