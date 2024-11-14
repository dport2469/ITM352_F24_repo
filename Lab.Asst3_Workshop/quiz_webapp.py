#Import the random module to randomize the order of the questions and options
import random
#Import the questions, options, explanations and answers from the json file
import json

from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
    global question_items, question_num, results
    #Randomize the order of the questions displayed
    question_items = shuffle_questions(selected_questions)
    question_num = 1
    results = []
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def thequiz():
    score = 0
    correct_answers = []
    total_time = 0
    bonus_points = 0
    global question_items, question_num, results

    if request.method == 'POST':
        # Logic to capture the user’s answers and redirect to the another question or result page

        # did the user answer correctly?
        user_answer = request.form.get('answer')
        if user_answer == question_items[question_num - 1][1]['correct']:
            results.append("Correct!")
        else:
            results.append("Incorrect!")
        # out of questions? send to results
        if question_num == len(question_items):
            return render_template('result.html', the_results = results)
        question_num = question_num + 1
    # Load the question and options to display
    the_question = question_items[question_num - 1]
    return render_template('quiz.html', question = the_question, q_num = question_num)  # Displays the question and options

@app.route('/result')
def result():
    global results
    # Calculate and display the user's score
    print(results)
    return render_template('result.html', the_results = results)

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