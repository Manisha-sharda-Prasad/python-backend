import random                                    # -randint function- in -random module-

highest = 10
answer = random.randint(1, highest)
print(answer)                                   # TODO : Remove after testing
guess = 0
print("please guess no. between 1 and {}: ".format(highest))

while guess != answer:                          # != is not equal to
    guess = int(input())
    if guess == 0:
        break
    if guess == answer:                          # != less than
        print("you got it first time")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:                                    # guess must be greater than answer
            print("Please guess lower")
        # guess = int(input())
        # if guess == answer:
        #     print("You got it right")
        # else:
        #     print("Sorry not guessed correctly")
        #
