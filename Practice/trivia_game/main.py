from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface
import os

script_dir = os.path.abspath(os.path.dirname(__file__))
true_img_path = os.path.join(script_dir, "images", "true.png")
false_img_path = os.path.join(script_dir, "images", "false.png")

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

print("True image path:", true_img_path)
print("False image path:", false_img_path)