from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    text = question["text"]
    answer = question["answer"]

    question_bank.append(Question(text, answer))


quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_question():
    quiz_brain.next_question()

print(f"""
You have completed the quiz
Your final score is {quiz_brain.score}/{quiz_brain.question_index}
""")
