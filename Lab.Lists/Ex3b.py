# Step 1: Create the initial list of responses
responses = [5, 7, 3, 8]

# Step 2: Add the response "0" to the end of the list
responses = responses + [0]

# Step 3: Insert the response "6" into the list at the third position
# The third position in a 0-indexed list is index 2
responses = responses[:2] + [6] + responses[2:]

# Step 4: Print out the list to verify the changes
print(responses)
