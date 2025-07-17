a = 12                      # expression:-  = + - * // %   , assigning 12 ,3 value to variable.
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)                  # float result , in decimal
print(a//b)                 # integer division use double//
print(a % b)

for i in range(1, a//b):    # (i)  is bound to each of the values produce by (range ).
    print(i)

# test:----
bun_price = 2.40
money = 15
print(15//2.40)

# Operator Precedence:-
print(a + b / 3 - 4 * 12)
print(a + (b / 3) - (4 * 12))
print(((a + b) / 3 - 4) * 12)   # right way
# Also---
c = a + b
d = c / 3
e = d - 4
f = e * 12
print(f)


