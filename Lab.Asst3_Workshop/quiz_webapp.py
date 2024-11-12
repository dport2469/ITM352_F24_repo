#Import the random module to randomize the order of the questions and options
import random
#Import the questions, options, explanations and answers from the json file
import json

from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
    global question_items
    #Randomize the order of the questions displayed
    question_items = shuffle_questions(selected_questions)
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def thequiz():
    score = 0
    correct_answers = []
    total_time = 0
    bonus_points = 0
    global question_items

    if request.method == 'POST':
        # Logic to capture the user’s answers and redirect to the result page
        return redirect(url_for('result'))
    # Load the question and options to display
    the_question = question_items[0]
    return render_template('quiz.html', question = the_question)  # Displays the question and options

@app.route('/result')
def result():
    # Calculate and display the user's score
    thescore = 1  # Example score for demonstration
    return render_template('result.html', score=thescore)

#Used a defined function here for reusability and readability
def shuffle_questions(questions):
    question_items = list(questions.items())
    random.shuffle(question_items)
    return question_items 

def main():
    global selected_questions
    #Read questions from json file
    with open('questions.json', 'r') as file:
        QUESTIONS = json.load(file)
    selected_category = 'Music'
    selected_questions = QUESTIONS[selected_category]

if __name__ == '__main__':
    main()
    app.run(debug=True)