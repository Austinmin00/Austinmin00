from Questions import Question


questions_prompts = [
    "How many legs does a spider have?\n(a) 2\n(b) 8\n(c) 6\n\n",
    "What is a monkey's favorite fruit?\n(a) Coconut\n(b) Apples\n(c) Bananas\n\n",
    "What part of the body does a bird use to fly?\n(a) Wings\n(b) Feet\n(c) Eyes\n\n"

]

questions = [
    Question(questions_prompts[0], "b"),
    Question(questions_prompts[1], "c"),
    Question(questions_prompts[2], "a"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt).lower()
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")
    if score == len(questions):
        print("Congratulations on passing Apollo's childrens test!")
    else:
        print("It seems you got a few wrong here. Please try again next time to earn yourself a passing score!")

run_test(questions)
