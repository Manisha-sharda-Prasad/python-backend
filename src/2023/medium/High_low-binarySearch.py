low = 1
high = 1000

print("Please think a no. between {} and {}".format(low, high))
input("press enter to start!!")

guesses = 1
while low != high:
    # print("\tGuessing in the range of {} to {}".format(low, high))
    guess = low + (high-low) // 2                    # formula to calculate the midpoint b/w the low and high values
    high_low = input("My guess is {}. Should I guess high or low? "
                     "Enter h, l or c if my guess is correct ".format(guess)).casefold()
    if high_low == "h":                              # higher- h, lower- l, correct-
        low = guess + 1                              # Guess high, the low end of the range becomes 1 greater than guess

    elif high_low == "l":
        high = guess - 1                             # Guess lower, the high end of the range becomes one less

    elif high_low == "c":
        print(" I got it in {} guesses!".format(guesses))
        break
    else:
        print(" ")
    # guesses = guesses + 1
    guesses += 1
else:
    print("You thought of the number {}".format(low))
    print(" I got it in {} guesses!".format(guesses))
