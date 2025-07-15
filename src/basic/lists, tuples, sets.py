#🔹 1. Lists-------------
#Mutable, ordered collection

#Can store mixed data types

fruits = ["apple", "banana", "cherry"]
print(fruits[0])         # apple
fruits.append("orange")  # Add element
print(fruits)
fruits.remove("banana")  # Remove element
print(len(fruits))       # Length

#🔹 2. Tuples-----------
#Immutable, ordered collection


colors = ("red", "green", "blue")
print(colors[1])        # green
print(len(colors))      # 3

# colors[0] = "yellow" → ❌ Error


#🔹 3. Sets-------------
#Unordered, no duplicates

nums = {1, 2, 3, 2, 1}
print(nums)             # {1, 2, 3}

nums.add(4)
nums.remove(2)
print(nums)             # {1, 3, 4}


#🔹 4. Dictionaries-------------
#Key-value pairs

#Unordered (in versions < 3.7)

student = {"name": "Alice", "age": 21, "major": "CS"}

print(student["name"])         # Alice
student["age"] = 22            # Update value
student["grade"] = "A"         # Add new key-value pair
print(student.keys())          # dict_keys(['name', 'age', 'major', 'grade'])
print(student.values())        # dict_values(['Alice', 22, 'CS', 'A'])


#🔹 5. String Methods & Slicing------------

text = "hello world"

print(text.upper())        # HELLO WORLD
print(text.capitalize())   # Hello world
print(text.replace("world", "Python"))  # hello Python
print(text.split())        # ['hello', 'world']

# Slicing:
print(text[0:5])           # hello
print(text[-5:])           # world


#🔹 6. List Comprehensions--------------
#Compact way to create a list

# Squares of numbers 1–5
squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# Even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(evens)    # [0, 2, 4, 6, 8]


#🔹 7. Nested Loops & Nested Dictionaries------------

#✅ Nested Loops:

for i in range(1, 4):
    for j in range(1, 3):
        print(f"i={i}, j={j}")

#✅ Nested Dictionary:

students = {
    "101": {"name": "Alice", "age": 21},
    "102": {"name": "Bob", "age": 22}
}
print(students["101"]["name"])  # Alice

# Loop through nested dict
for id, info in students.items():
    print("ID:", id)
    for key, value in info.items():
        print(f"  {key}: {value}")
