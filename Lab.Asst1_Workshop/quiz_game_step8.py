# quiz.py - an interactive quiz system, eighth version
# - Make QUESTIONS a dictionary, to include answer options and the correct choice.
# - Allow the user to select the correct answer by its label.
# - Improve the look and usability.  Keep track of correct answers. Loop until a user
#   provides a correct alternative.
# - Randomize the order of questions and order of the answer alternatives per question
# - Refactor the code to use functions
# - Put the questions into a JSON file and read from it.

from string import ascii_lowercase
import random
import json

# Read in and load the file of quiz questions
f = open('questions.json')
NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS = json.load(f)

# Functions for main processing steps
def prepare_questions(questions, num_questions):
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions)

def get_answer(question, alternatives):
    print(f"{question}?")
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please answer one of {', '.join(labeled_alternatives)}")

    return labeled_alternatives[answer_label]

def ask_question(question, alternatives):
    correct_answer = alternatives[0]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answer = get_answer(question, ordered_alternatives)
    if answer == correct_answer:
        print("⭐ Correct! ⭐\n")
        return 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}\n")
        return 0


# Main quiz steps: preparing questions, running the quiz, giving feedback
questions = prepare_questions(QUESTIONS, num_questions=NUM_QUESTIONS_PER_QUIZ)

# Process (main loop)
num_correct = 0
for num, (question,alternatives) in enumerate(questions,start=1):
    print(f"Question {num}: ")
    num_correct += ask_question(question,alternatives)

# Postprocess
print(f"\nYou got {num_correct} correct. Thank you for playing!")