from oldquestions import questions_old

questions_prompts = [
    "Who invented the windmill?\n(a) Will Kamkwamba\n(b) Hank Millheuse\n(c) Elon Tusk\n\n",
    "What is the chemical compund for Nitrite?\n(a) Na2S2O5\n(b) N2O\n(c) NO2\n\n",
    "Which state is closest to texas?\n(a) Missouri\n(b) Montana\n(c) Tennessee\n\n"

]

questions = [
    questions_old(questions_prompts[0], "a"),
    questions_old(questions_prompts[1], "c"),
    questions_old(questions_prompts[2], "a"),
]

def run_old_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt).lower()
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")
    if score == len(questions):
        print("Congratualtions, you have passed Apollo's adults test!")
    else:
        print("It seems you've gotten a few wrong. Try again next time to earn a passing grade.")

run_old_test(questions)
