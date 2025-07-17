string1 = "Hi there! "
string2 = "i am "
string3 = "Manisha  "
string4 = "i am learning "
string5 = "Python 3. "
print(string1 + string2 + string3 + string4 + string5)
# also---
print("Hi there! " "i am " "Manisha Prasad " "i am learning " "Python 3. ")
# Strings can be multiplied --
print("Hello" * 3)
print("Hello" * (3+4))
print("Hello" * 3 + "4")
# test--
quantity = 10
price = 5.0
total = quantity * price
tax = total/5
total = total + tax
print(total)               # doses nt include tax so ans.- 50.0 only
# total (10   * 5.0 = 50.0)
# tax   (50.0  /  5 = 10.0)
# total (50.0 + 10.0= 60.0)


today = "friday"
print("day" in today)             # t
print("friday" in today)          # t
print("saturday" in today)        # f
