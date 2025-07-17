# mutable object is one whose value can be changed.
# examples of mut.-- list, dict(dictionaries), set, Bytearray
shopping_list = ["milk",
                 "bread",
                 "eggs",
                 "ginger",
                 "onions"
                 ]
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))
# cookies added in the shopping_list- concatenate, without adding new object, new str, and not needed to reattach.
shopping_list += ["cookies"]
print(shopping_list)                         # we mutated our list
print(id(shopping_list))                     # id is still same, mutable


