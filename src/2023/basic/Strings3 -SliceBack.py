parrot = "Norwegian Blue"
#   N   o   r   w   e   g   i   a   n       B   l   u   e            characters
#   0   1   2   3   4   5   6   7   8   9   10  11  12  13           Positive Index
#   14  14  14  14  14  14  14  14  14  14  14  14  14  14
#  -14 -13 -12 -11 -10 -9  -8  -7  -6  -5  -4   -3  -2  -1           Negative Index

# Negative Index = Positive Index - size(14)
# slicing : [start: end-index +1]

# Slicing:----positive & negative nos.----

#1 ::Norwegian Blue
print(parrot, parrot[:], parrot[0:], parrot[0:parrot.__sizeof__()])

#2 :: wegian
print(parrot[3:9], parrot[-11:-5], parrot[-11:9])

#3 :: lu
print(parrot[11:13], parrot[-3:-1])
print(parrot[-3:])                        # end index = size

#4 :: lueNor
print(parrot[-3:] + parrot[:-11])

# Step in a Slice / with positive step :--------
#5 :: ow
print(parrot[1:4:2])
#6 :: wi u
print(parrot[3::3])


# Slicing Backwards / with negative step :-------

#7 :: eulb
print(parrot[13:9:-1])

#8 :: nierN
print(parrot[8::-2])

#9 :: ae
print(parrot[7:2:-3])

#10 :: BlueNorweg :(
# print(parrot[10:6:1])

# enteredWord = input("Enter a word : ")
# print ('actual word : ', enteredWord)
# reverseWord = enteredWord[::-1]
# print('reverse word : ', reverseWord)
# if(enteredWord  == reverseWord):
#     print('yes palindrome')

# test--
# including ,comma and space---
# slice starts at first character, includes every 5th character--
#                   1    1    2     2     3
#    01234 56789 01234 56789 21234 56789  012
days = "mon, tue, wed, thu, fri, sat, sun"
# ['m','o','n',',', ' ','t']
x1 = ["mon","tues",]
x2 = [['m','o','n'],  ['t','u','e', 's']]
print(x1[1][2])

print(days[::5])
