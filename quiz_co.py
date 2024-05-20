class Questions:
    def __init__(self, prompt, ans):
        self.prompt = prompt
        self.ans = ans

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_quiz(self):
        for i in range(len(self.questions)):
            us_ans = input(self.questions[i].prompt + "\n")
            if us_ans.lower() == self.questions[i].ans.lower():
                self.score += 1
        print("Total score: ", self.score, "out of:", len(self.questions))

question_prompts = [
    "What is he capital of India? \na)Tamil Nadu \nb)Kerala \nc)Delhi \nd)Bangalore",
    "Who invented python programming Language? \na) Guido van Rossum \nb)Elon Musk \nc)James Gosling \nd)Dennis Ritchie",
    "Python is written in \na) c++\nb) c\nc) java \nd)Forton",
    "Is python an object oriented programming \na)Yes \nb)NO \nc)Maybe \nd)no idea"
]
ques = [
    Questions(question_prompts[0], "c"),
    Questions(question_prompts[1], "a"),
    Questions(question_prompts[2], "b"),
    Questions(question_prompts[3], "a")
]
quiz = Quiz(ques)
quiz.display_quiz()
