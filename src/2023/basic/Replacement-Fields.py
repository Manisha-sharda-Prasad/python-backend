age = 27
# print("my age is" + str(age) + " years")
# also--
print("my age is {0} years" .format(age))

# We used 8 replacement fields - no. from 0 to 7,
# These replaced with the values in the ( parentheses ) after .format---

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "Jan", "March", "May", "Jul", "Aug", "Oct", "Dec"))
# also--
# 1--
print("There are {0} days in Jan, March, May, Jul, Aug, Oct, Dec" .format(31))
# 2--
print("Jan : {2}, Feb : {0}, March : {2}, Apr : {1}, May : {2}, Jun : {1}, Jul : {2}, "
      "Aug : {1}, Sep :{2}, Oct : {1}, Nov : {2}, Dec : {1}"
      .format(28, 30, 31))
print()
print("My age is {0}, my brother is {1} year older than me and our nephew is {2} years old.".format(27, 1, 5))

# eg--.format({0},{1},{2})
# also--
# 3--
print(""""
Jan : {2}
Feb : {0}
Mar : {2}
Apr : {1}
May : {2}
Jun : {1}
Jul : {2}
Aug : {1} 
Sep : {2} 
Oct : {1}
Nov : {2}
Dec : {1}
      """.format(28, 30, 31))

# test---
flower = "rose"
colour = "red"
print("The {0} is {1}".format(flower, colour))
print("My favourite flower is {0} {1}".format(colour, flower))


