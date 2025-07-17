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
