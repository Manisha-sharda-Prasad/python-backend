number = "9,23,45; 45:689,0"
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

print(separators)                                                           # ,,; :,
print(number)                                                               # 9,23,45; 45:689,0

# number = input("Enter a series of numbers, using any separators you like: ")
# separators = ""
#
# for char in number:
#     if not char.isnumeric():
#         separators = separators + char
#
# print(separators)                                                           # ,,; :,
# print(number)                                                               #
quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.
for char in quote:
    if char.isupper():
        print(char)
