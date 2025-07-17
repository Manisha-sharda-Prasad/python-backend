# print("Welcome to my-Instagram. Please signup")
# username = input("Enter user name ")
# password = input("Enter you password ")
# securityAnswer1 = input("security question 1 : Enter year of birth ")
# securityAnswer2 = input("security question 1 : Enter marriage Year ")
# print("Signup SuccessFul ! \n\nLogin Now\n")
#
# username_input = input("username :: ")
# password_input = input("password :: ")
#
# if password == password_input:
#     print("Welcome "+username_input)
# else:
#     print("Wrong password")
#     print()

activity = input("What would you like to do today?")

if "draw" not in activity.casefold():
    print("But i want to draw today!!")
elif "dance" in activity:                           # won't work coz if
    print("I wanna learn dance today!!")
else:
    print("do what you like!!")
print()


