#✅ Variables:
#Variables are used to store data.

name = "Alice"       # String
age = 25             # Integer
height = 5.6         # Float
is_student = True    # Boolean

#✅ Data Types:
#int, float, str, bool, list, tuple, dict, set.

#✅ Input/Output:

# Input from user
name = input("Enter your name: ")
print("Hello,", name)

# Converting input to int/float
age = int(input("Enter your age: "))
print("In 5 years, you'll be", age + 5)

#🔹 2. Operators & Conditionals (if/else)
#✅ Operators:
#Arithmetic: +, -, *, /, //, %, **

#Comparison: ==, !=, <, >, <=, >=

#Logical: and, or, not


a = 10
b = 3
print(a + b)   # 13
print(a % b)   # 1
print(a > b)   # True
print(a > b and b < 5)  # True

#✅ Conditionals:

age2 = int(input("Enter your age: "))

if age2 < 18:
    print("Minor")
elif age2 < 65:
    print("Adult")
else:
    print("Senior")

#🔹 3. Loops (for, while), range()
#✅ For Loop:

for i in range(5):   # 0 to 4
    print("i =", i)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#✅ While Loop:

count = 0
while count < 3:
    print("Count:", count)
    count += 1

#✅ range(start, stop, step):

for i in range(1, 10, 2):
    print(i)  # Prints 1, 3, 5, 7, 9

#🔹 4. Functions (def, return, parameters)
#✅ Basic Function:

def greet():
    print("Hello!")

greet()  # Output: Hello!


#✅ Function with Parameters:

def greet(name2):
    print("Hello,", name)

greet("Manisha")  # Output: Hello, Manisha

#✅ Function with Return Value:

def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)

#✅ Default Parameters:

def greet(name="Guest"):
    print("Hello", name)

greet()          # Hello Guest
greet("Anya")    # Hello Anya
