import random


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0
        self.already_asked = []

    def q_already_asked(self, next_question):
        already_asked = False
        for question in self.already_asked:
            if question.text == next_question.text:
                already_asked = True
                return already_asked
        return already_asked

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
            print(f"The correct answer was: {correct_answer}.")
            print(f"Your score is: {self.score}/{self.question_number}\n\n")

    def next_question(self):
        self.question_number += 1

        next_question = random.choice(self.questions_list)
        while self.q_already_asked(next_question):
            next_question = random.choice(self.questions_list)

        self.already_asked.append(next_question)
        users_answer = input(f"Q.{self.question_number}: {next_question.text} (True/False): ")
        self.check_answer(users_answer, next_question.answer)
