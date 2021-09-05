from question_data import question_data
from quiz_methods import *


elist = []

for i in question_data:
    # Loads each question("text") and answer in question_data
    # into Question class seperately and adds all into list "elist" initialization.
    elist.append(Question(i["text"], i["answer"]))
#print(elist)

# Initializes QuizBrain class by inputing elist which contains list of quiz questions
quiz = QuizBrain(elist)
print(quiz.next_quest())