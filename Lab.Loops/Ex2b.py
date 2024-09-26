even_numbers = [2]

while even_numbers[-1] <= 48:
    even_numbers.append(even_numbers[-1] + 2)

print(even_numbers)