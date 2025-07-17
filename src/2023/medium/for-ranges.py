# temp = range(0,5)
# print(temp.__sizeof__())

for i in range(0, 10):                                      # 10 excluded 1-9 , don't need to include 0
    print("i is now {}".format(i))                          # i is for index

for i in range(0, 20, 2):                                   # 2 steps, don't need to include 0
    print("i is now {}".format(i))
print()

for i in range(10, 0, -2):                                   # -2 steps, opposite direction -starts from 10.
    print("i is now {}".format(i))
print()

for i in range(0, 101):
    if i % 7 == 0:
        print(i)
print()
# e.g. of Break---
# code inside this loop to stop when -i is greater than 0 and exactly divisible by 11
for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break
print()
# e.g. of Continue---
# print all the numbers from 0 to 20 that aren't divisible by either 3 or 5.
for x in range(21):
    if x % 3 == 0 or x % 5 == 0:
        continue
    print(x)

print()
age = int(input("how old are you ??"))
if age in range(16, 59):
    print("You can get a surgery!!")
else:
    print("Sorry, maybe medication can help!!")
