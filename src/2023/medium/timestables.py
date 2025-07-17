for i in range(1, 13):                                            # (1, 12 )
    for j in range(1, 13):                                        # {0} times {1} is {2}
        print("{0} times {1} is {2}".format(j, i, i * j))         # {1} *{1} ={1}, 2*1=2, 3*1=3.....1*2, 2*2, 3*2....
    print("_______________________")
