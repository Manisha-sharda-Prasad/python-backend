# and, or conditions----
age = int(input("how old are you?"))

# if age >= 16 and age <= 58:
# also- use range:-
# if age in range(16, 59):
if 18 <= age <= 58:                                       # if age is greater or equal to 18 less or equal to 58.
    print("You can get a surgery!!")
else:
    print("Sorry, maybe medication can help!!")

print("_-" * 15)                                          # for gap /design -___-___- 15 range
yourAge = int(input("how old are you?"))
if yourAge < 16 or yourAge > 35:                                  # if age less than 16 and greater than 35.
    print("Sorry, you can not play the game!!")
else:
    print("You can play the game!!")
