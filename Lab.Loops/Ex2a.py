even_numbers = []
number = 1

while number <= 50:
    if number % 2 == 0:
        even_numbers.append(number)
    number += 1

print(even_numbers)