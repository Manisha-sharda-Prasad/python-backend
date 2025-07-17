# Else in a loop-------
numbers = [1, 45, 31, 16, 60]

for number in numbers:
    if number % 8 == 0:                           # reject the list
        print("the numbers are acceptable!!")
        break
else:                                     # else is associated with the for loop, not with if statement.
    print("All those numbers are fine!!")
