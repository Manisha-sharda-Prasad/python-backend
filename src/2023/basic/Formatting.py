for i in range(1, 12):
    print("No. {0} squared is {1} and cubed is {2}".format(i, i ** 2, i ** 3))
# also--
print(" ")
for i in range(1, 12):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))
# also--
# more clean and align--
print(" ")
for i in range(1, 12):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))
print()
# maximum precision of a python floating-point is b/w 51 & 53 digits:----
print("Pi is approximately {0:12}".format(22/7))
print("Pi is approximately {0:12f}".format(22/7))
print("Pi is approximately {0:12.50f}".format(22/7))
print("Pi is approximately {0:52.50f}".format(22/7))
print("Pi is approximately {0:62.50f}".format(22/7))
print("Pi is approximately {0:72.50f}".format(22/7))
print("Pi is approximately {0:<72.54f}".format(22/7))
print()
