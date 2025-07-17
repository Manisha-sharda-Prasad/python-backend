# day = "Monday"
# temperature = 30
# raining = True

day = "Friday"
temperature = 30
raining = False

if (day == "Saturday" and temperature > 27) or not raining:    # replaced and with or //use() if "or""and" in same code.
    print("GO SWIMMING")                                       # and has a higher precedence than or
else:
    print("STAY HOME")

# if 0:
#     print("True")                                             # 0 evaluates false.
# else:
#    print("False")

name = input("please enter your name:")
# if name :
if name != "":
    print("hello, {}".format(name))
else:
    print("you don't have a name?")


