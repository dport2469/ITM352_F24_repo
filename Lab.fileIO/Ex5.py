import json

quiz_data = {
     "What is the airspeed of an unladen swallow in miles/hr": [
          "12",
          "8",
          "11",
          "15"
     ],
     "What is the capital of Texas": [
          "Austin",
          "San Antonio",
          "Dallas",
          "Waco"
     ],
     "The Last Supper was painted by which artist": [
          "Da Vinci",
          "Rembrandt",
          "Picasso",
          "Michelangelo"
     ],
     "Which classic novel opens with the line 'Call Me Ishmael'?": [
          "Moby Dick",
          "Wuthering Heights",
          "The Old Man and the Sea",
          "The Scarlet Letter"
     ],
     "Frank Lloyd Wright designed a house that included a waterfall. What is the name of this house?": [
          "Fallingwater",
          "Watering Heights",
          "Mossyledge",
          "Taliesin"
     ]
}

quiz_data_json = json.dumps(quiz_data)

quiz_data_file = open('quiz_questions.json', 'w')
quiz_data_file.write(quiz_data_json)
quiz_data_file.close()