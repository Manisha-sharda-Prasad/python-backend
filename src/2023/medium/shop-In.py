shopping_list = ["milk", "bread", "eggs", "ginger", "onions"]

for item in shopping_list:
    if item != "eggs":                                          # if item is not equal to eggs-- exclude eggs
        print("Buy " + item)
print(" ")
# also  use-- Continue--

for item in shopping_list:
    if item == "eggs":                                          # if item is equal to eggs-- exclude eggs
        continue
    print("Buy " + item)
print(" ")
#  use-- Break--

for item in shopping_list:
    if item == "bread":                                          # if item is equal to bread--break after bread
        break
    print("Buy " + item)

