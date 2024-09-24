# Define the list of survey response values
survey_responses = [5, 7, 3, 8]

# Define the tuple of respondent ID values
respondent_ids = (1012, 1035, 1021, 1053)

# Append the tuple to the list
survey_data = dict(zip(respondent_ids, survey_responses)) 

# Print the Dictionary
print(survey_data)