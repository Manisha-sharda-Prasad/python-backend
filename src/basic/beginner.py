#🔹 1. Variables, Data Types, Input/Output--------------

#✅ Data Types:

"""
*int, float, str, bool, list, tuple, dict, set.
Text Type:	    str
Numeric Types:	int, float, complex(j)
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	    set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memory-view
None Type:	    NoneType
"""
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


# ---------Type Conversion-----------
print('🔸--Type Conversion  -- ')
x = 1   #int
y = 3.5 #float
z = 5j  #complex

a = float(x)
b = complex(y)
c = int(x)

print(a, b, c)
print(type(a), type(b), type(c))

# ---------Casting-----------
print('🔸--Casting  -- ')
#Integer:
k = int(1)      #  1
l = int(2.8)    #  2
m = int("3")    #  3

#Floats:
n = float(1)     #  1.0
o = float(2.8)   #  2.8
p = float("3")   #  3.0
q = float("4.2")

#Strings:
r = str("s1")
s = str(2)         #'2'
t = str(3.0)
