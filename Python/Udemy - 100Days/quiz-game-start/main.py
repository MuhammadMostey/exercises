from data import question_data
from data import question_data_trivia
from question_model import Question
from quiz_brain import QuizBrain


# Questions from question_data Game
question_bank = []
for question_object in question_data:
    ques = question_object["text"]
    ans = question_object["answer"]
    question_bank.append(Question(ques, ans))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


# Questions from question_data_trivia Game
question_bank_trivia = []
for question_object in question_data_trivia:
    ques = question_object["question"]
    ans = question_object["correct_answer"]
    question_bank_trivia.append(Question(ques, ans))

quiz_trivia = QuizBrain(question_bank_trivia)

while quiz_trivia.still_has_questions():
    quiz_trivia.next_question()
