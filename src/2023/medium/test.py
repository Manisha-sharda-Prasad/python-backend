# activity_to_do = ["1.Learn Python", "2.Learn Java", "3.Go Swimming", "4.Have Dinner", "5.Go to Bed", "6.Exit"]

# print("Please choose any activity from below: ")
# print("1:\tLearn Python")
# print("2:\tLearn Java")
# print("3:\tGo Swimming")
# print("4:\tHave Dinner")
# print("5:\tGo to Bed")
# print("0:\tExit")
choice = "_"

while choice != "0":
    if choice in "12345":
        print("You chose {}".format(choice))
    else:
        print("Please choose any activity from below: ")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo Swimming")
        print("4:\tHave Dinner")
        print("5:\tGo to Bed")
        print("0:\tExit")
    choice = input()
