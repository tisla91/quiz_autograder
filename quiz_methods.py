class Question:
    """Takes in a question and a preset answer from user on every initialization."""

    def __init__(self, text, answer):
      self.text = text
      self.answer = answer

new_q = Question("What is my name?", "Isaac")
# print(new_q.text)
# print(new_q.answer)


class QuizBrain:

    """Takes a set of preset questions and answers as input, and
     displays each at a time, keeping record of user score."""
    def __init__(self, q_list):
        self.question_no = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        # Checks if it is the last question in question list(q_list)
        if self.question_no < len(self.question_list):
            return False
        else:
            return True

    def next_quest(self):
        # Displays questions in self.question_list one after the other.
        for i in range(len(self.question_list)):
            self.question_no = i + 1

            # Checks to make sure user enters correct answer options.
            while True:
                user_ans = input(f"Q.{self.question_no}: {self.question_list[i].text} (True/False)?:\n")
                if user_ans in ["True", "False"]:
                    break
                else:
                    print('Please answer "True" or "False"')
            # keeps count of candidate score through the quiz
            if user_ans.lower() == self.question_list[i].answer.lower():
                self.score = self.score + 1
                print("You got it right!")
            elif user_ans != self.question_list[i].answer:
                print("You got it wrong!")
            print(f"The correct answer was: {self.question_list[i].answer}")
            print(f"Your current score is: {self.score}/{self.question_no}")
            print("\n")
        print(f"You have come to the end of the quiz\n Yoour overall score is {self.score}/{self.question_no}")
