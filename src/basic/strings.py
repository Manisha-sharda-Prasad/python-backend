#----------Slicing Strings---------
print('🔸--Slicing Strings -- ')

word = "Hey Bonita"
print(word[2:5])        # y_B           / step 1   --->
print(word[3:8])        # _Boni
print(word[-4:-9:-1])   # noB_y        / step -1   <---   Negative Indexing

word1 = "0123456789"   # start_i, end_i+1, steps + - / -10....-4-3-2-1
print(word1[-4::1], word1[6::1], word1[-4:-6:-1])     # 6789, 6789, 65

#------------Modify Strings----------
print('🔸--Modify Strings -- ')

w = " Modify, Strings!! "

print(w.split(","))
print(w.upper(),w.lower())
print(w.strip())


#------------ String Concatenation ----------
print('🔸--String Concatenation -- ')

#combine, two strings +

n = "Lekh"
o = "Isha"
p = n + o
print(p)
print(p.capitalize())


#------------ Format /F Strings ----------
print('🔸-- Format - Strings -- ')

age = 36
txt = f"My name is John, I am {age}"
print(txt)

# Placeholders and Modifiers
#placeholder can contain vars, operations, functions,modifiers to format the value.

price = 59
txt = f"Your final price with coupon is {price - 5} dollars"
print(txt)
txt = f"Your final price with coupon is {price :.2f} dollars"  # 2 decimals = 59.00 / .3f = 59.000
print(txt)

