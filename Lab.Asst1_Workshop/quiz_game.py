score = 0
questions = ("What is the airspeed of an unladen swallow in miles/hr", "What is the capital of Texas")
answers = ("12", "Austin")

for question_num in range(1,len(questions)):
    answer = input(f"{question_num}. {questions[question_num - 1]}? ")
    if answer == answers[question_num - 1]:
        score = score + 1

print(f"Your score is {score}")