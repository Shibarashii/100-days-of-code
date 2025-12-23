class QuizBrain:
    def __init__(self, question_list):
        self.question_index = 0
        self.score = 0
        self.question_list = question_list

    def still_has_question(self):
        return self.question_index < len(self.question_list)

    def check_answer(self, choice, current_answer, question_number):
        result = "You got it right" if choice.lower() == current_answer.lower() else "You got it wrong"
        if choice.lower() == current_answer.lower():
            print(f"{result} \nThe correct answer was: {current_answer}")
            self.score += 1
            print(f"Your current score {self.score}/{question_number}")
            self.question_index += 1
        else:
            print(f"{result} \nThe correct answer was: {current_answer}")
            print(f"Your current score {self.score}/{question_number}")
            self.question_index += 1

    def next_question(self):
        current_question = self.question_list[self.question_index]
        question_number = self.question_index + 1
        choice = input(f"Q.{question_number}: {current_question.text} (True/False)? ")

        self.check_answer(choice, current_question.answer, question_number)


