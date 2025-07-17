name = input("Enter your name:")

age = int(input("Enter your age:"))

if 18 <= age <= 30:                             # or if age < 18 or age > 30:
    print("Welcome to your holiday,{0}".format(name))
else:
    print("Sorry you dont have a holiday! :(")

