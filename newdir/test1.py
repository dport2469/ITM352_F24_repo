# Original tuple
original_tuple = (1, 2, 3)

try:
    # Try to modify the tuple
   original_tuple.append(4)  # This will raise an error

except Exception as e:
    # Convert the tuple to a list
    temp_list = list(original_tuple)

    # Append 'Z' to the list
    temp_list.append("Z")

    # Convert the list back to a tuple
    original_tuple = tuple(temp_list)

# Print the new tuple
print(original_tuple)