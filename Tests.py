print("Hello, welcome to Apollo's testing site!")
print(" Please enter some imfortmation for us so we can understand\n \
who you are, your age, and whether or not you are eligible\n \
to take the childrens test or the adults test.")
print("For the childrens test the age range is 5-15.")
print("For the adults test the age range is 16-30.")
name = input("Enter your name: ")
print("Well hello there " +  name + "!")
print("May I get your age to start off what exam you'll be taking today?")
age = input("Enter your age: ")
print("Thank you so much! It seems you enetered " + age + " is that correct?")

correct_answer = "yes"
answer = ""
wrong_answer = "no"

while answer != correct_answer:
    answer = input("Enter yes or no: ")
    if answer == wrong_answer:
        age = input ("please enter the correct age: ")
        print("is this correct now?")
    
if correct_answer:
    print("Excellent, on to your test.")


old_test = 16
if int(age) >= old_test:
    from oldprompts import run_old_test
else:
    from prompts import run_test


