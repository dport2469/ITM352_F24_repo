score = 0
qas = {
    "What is the airspeed of an unladen swallow in miles/hr": "12",
    "What is the capital of Texas": "Austin"
}

for question_num, (question, answer) in enumerate(qas.items(), start=1):
    user_answer = input(f"{question_num}. {question}? ")
    if user_answer == answer:
        score += 1

print(f"Your score is {score}")
