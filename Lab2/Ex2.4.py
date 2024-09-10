# Ask user for a number using stdin
number = float(input("Enter a decimal formatted number between 1 and 100: "))
# print out the square of the input
square_num = round(number ** 2, 2)
print("The square of "+ str(number) + " is " + str(square_num) )