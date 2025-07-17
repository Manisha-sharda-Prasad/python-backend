# Initialising Variables and None--
shopping_list = ["milk", "bread", "eggs", "ginger", "onions"]

item_to_find = "bread"
# item_to_find = "albatross"
found_at = None                                             # None equivalent to Null, something doses nt have a value.

# we shouldn't use like this --
# for index in range(6):
# for index in range(len(shopping_list)):                     # len is length - of shopping list
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break
# right way --
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)
if found_at is not None:
    print("Item found at position {}".format(found_at))         # print-1----0,1,2....
else:
    print("{} not found".format(item_to_find))                  # will show--None

