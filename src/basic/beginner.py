#🔹 1. Variables, Data Types, Input/Output--------------
#✅ Data Types:
#int, float, str, bool, list, tuple, dict, set.

#✅ Variables:
# Variables are used to store data.

name = "Alice"       # String
age = 25             # Integer
height = 5.6         # Float
is_student = True    # Boolean

#✅ Input/Output:

# Input from user
school = input("Enter your school: ")
print("Your school is:" ,school)

# Converting input to int/float
age1 = int(input("Enter your age: "))
print("In 5 years, you'll be", age1 + 5)


print('🔸-- input_output -- ')

idealWeight = 55
weight = int(input("Enter your weight: "))
if weight < 55:
    print("You should gain : " ,(idealWeight - weight), " kgs")
if weight > 55:
    print("You should not gain more, please loose : " ,(idealWeight - weight), " kgs")
if weight == 55:
    print("you have ideal weight")


#🔹 2. Operators & Conditionals (if/else)-------------
#✅ Operators:
#Arithmetic: +, -, *, /, //, %, **
#Comparison: ==, !=, <, >, <=, >=
#Logical:   and, or, not

print('🔸-- operator -- ')
a = 10
b = 3
print(a + b)   # 13
print(a % b)   # 1
print(a > b)   # True
print(a > b and b < 5)  # True


#✅ Conditionals:

print('🔸-- condition : if else-- ')

age2 = int(input("Enter your age: "))

if age2 < 18:
        print("Minor")
elif age2 < 65:
        print("Adult")
else:
        print("Senior")

#🔹 3. Loops (for, while), range()------------

#✅ For Loop:

print('🔸-- for_loop -- ')

for i in range(4):          # 0 to 3 / -4 to -1
    print("i =", i)

flowers = ["daisy", "rose", "sunflower", "jasmine"]
for fl in flowers:
    print(fl)

#✅ While Loop:
print('🔸-- while_loop -- ')

count = 0
while count < 3: # 0,1,2
    print("Count:", count)
    count += 1

litre = 1
while litre < 5:
    print("litre:", litre)
    litre += 2       # ignore (2+),  1-4


#✅ range(start, stop, step):
print('🔸-- range_loop -- ')

for i in range(1, 8, 2):  # ignore every 2nd *
    print(i)               # Prints 1, 3, 5, 7

for i in range(-8, -1, 1): # -10 to -2
    print(i)


