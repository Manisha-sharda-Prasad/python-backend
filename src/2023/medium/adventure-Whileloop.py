available_exits = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose direction: ")
    if chosen_exit.casefold() == "quit":     # case.fold used for if user types "quit" into -capitals "Quit"
        print("Game Over")
        break                               # break and continue in -while loop, break will stop the code after.
else:
    print("aren't you glad you got out of there")
