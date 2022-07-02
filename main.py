from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    text = question["question"]
    answer = question["correct_answer"]
    new_question = Question(text, answer)
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)

still_playing = True
while still_playing:
    quiz_brain.next_question()
    if quiz_brain.question_number == len(question_bank):
        print("That's all, folks! Thanks for playing.")
        still_playing = False
