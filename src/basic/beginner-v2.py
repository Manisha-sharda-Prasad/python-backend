#🔹 1. Variables, Data Types, Input/Output--------------
#✅ Data Types:
#int, float, str, bool, list, tuple, dict, set.

#✅ Variables:
# Variables are used to store data.
def variable_demo():
    name = "Alice"       # String
    age = 25             # Integer
    height = 5.6         # Float
    is_student = True    # Boolean

#✅ Input/Output:

# Input from user
#school = input("Enter your school: ")
#print("Your school is:" ,school)

# Converting input to int/float
#age1 = int(input("Enter your age: "))
#print("In 5 years, you'll be", age1 + 5)

def input_output_demo():
    print('🔸-- input_output_demo -- ')
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

def operator_demo():
    print('🔸-- operator_demo -- ')
    a = 10
    b = 3
    print(a + b)   # 13
    print(a % b)   # 1
    print(a > b)   # True
    print(a > b and b < 5)  # True


#✅ Conditionals:
def condition_demo():
    print('🔸-- condition_demo-- ')
    age2 = int(input("Enter your age: "))

    if age2 < 18:
        print("Minor")
    elif age2 < 65:
        print("Adult")
    else:
        print("Senior")

#🔹 3. Loops (for, while), range()------------

#✅ For Loop:
def for_loop_demo():
    print('🔸-- for_loop_demo -- ')
    for i in range(4):          # 0 to 3 / -4 to -1
        print("i =", i)

    flowers = ["daisy", "rose", "sunflower", "jasmine"]
    for fl in flowers:
        print(fl)

#✅ While Loop:
def while_loop_demo():
    print('🔸-- while_loop_demo -- ')
    count = 0
    while count < 3: # 0,1,2
        print("Count:", count)
        count += 1

    litre = 1
    while litre < 5:
        print("litre:", litre)
        litre += 2       # ignore (2+),  1-4


#✅ range(start, stop, step):
def range_loop_demo():
    print('🔸-- range_loop_demo -- ')
    for i in range(1, 8, 2):  # ignore every 2nd *
        print(i)               # Prints 1, 3, 5, 7

    for i in range(-8, -1, 1): # -10 to -2
        print(i)


# =========== main ========

print('\n🟪',"="*20, 'topic-1 :: basic', '='*20)
variable_demo()
input_output_demo()
operator_demo()
condition_demo()

print('\n🟪',"="*20, 'topic-2 :: loop', '='*20)
for_loop_demo()
while_loop_demo()
range_loop_demo()

