parrot= "Norwegian Blue"
#   N   o   r   w   e   g   i   a   n       B   l   u   e
#   0   1   2   3   4   5   6   7   8   9   10  11  12  13           characters
#  -14 -13 -12 -11 -10 -9  -8  -7  -6  -5  -4   -3  -2  -1           Negative Indexing
print(parrot)
print(parrot[3])
print(parrot[4])
print(" ")
print(parrot[3])
print(parrot[6])
print(parrot[8])
print(" ")
# Negative Index = Positive Index - size(14)
# slicing : [start: end-index +1]
# Negative Indexing:------
# print(parrot[-14])         # 0 = -14 shows same / 14 does nt exist , but it takes -14 as 0.
print(parrot[-11])           # from -> backwards    -1 = 13, -2 = 12
print(parrot[-10])
print(" ")
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])
print(" ")
# also:-
print(parrot[3-14])
print(parrot[4-14])
print(" ")
print(parrot[3-14])
print(parrot[6-14])
print(parrot[8-14])
print(" ")
# Slicing:----(positive)-------
print(parrot[:])               # take whole           -> [0-13]
print(parrot[0:6])             # [0:6]   6 get sliced -> [0:5]
print(parrot[10:])             # [10:14] blue or [10:] still blue
print(parrot[:9])
print(parrot[:4] + parrot[6:])
# Slicing:----(negative)-------
# Start value should be > greater than end value- 5:1, 12:7,4:2....
print(parrot[-11:-9])
print(parrot[-4:])
print(parrot[-1:])
print(parrot[1:])
print(parrot[:1])
print(parrot[0])

# for more go to --->> Strings 3-SliceBack-
