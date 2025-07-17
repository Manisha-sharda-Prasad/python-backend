# object than cannot be changed is called immutable, types---
# int, float, bool t/f, str, tuple, frozenset, bytes
result = True
another_result = result                     # both variables are bound to a value that is -bool -true
print(id(result))                           # id returns the identity of an object, returns object memory address.
print(id(another_result))

result = False                              # rebound result to a new value of -bool- false,
print(id(result))                           # bools are immutable, but we can change value from t to f.

print("----------------")

new_result = "correct"                       # str value of variable
second_result = new_result
print(id(new_result))
print(id(second_result))
# str are immutable,we tried to change but pyt created new object, new str, reattached name to it.
new_result += "ish"
print(id(new_result))                       # str value , but changed-id
print(id(second_result))                    # id still same, couldn't change
