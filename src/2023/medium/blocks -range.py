for i in range(1, 13):                                  # range b/w (1, 12)
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
    print("*" * 80)      # press tab or space to add/ indent this line in same code above...
print()
name = input("Please enter your name: ")
age = int(input("how old are you, {0}?".format(name)))  # int for integer
print(age)
# if age >= 18:
#     print("You are old enough to vote")
#     print("Please put an x in the box")
# include many elif parts, but else can be used one time.
if age < 18:
    print("cannot vote, Please come back in {0} years".format(18-age))
elif age == 900:
    print("Sorry, you are alien !!!")
else:
    print("You are old enough to vote")
    print("Please put an x in the box")
