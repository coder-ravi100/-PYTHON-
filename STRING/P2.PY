#FIND STRING FUNCTION :
#FIND FUNCTION IS RETURN THE POSITION OF SUB STRING
name = "Tops Technologies"
word1 = name.find("e")
word2 = name.find("To")
print(word1)
print(word2)
'''
✅Yeh function substring ka index number (position) return karta hai.
✅Agar substring nahi mile to -1 return karta hai.
✅start aur end optional hote hain, jaha se search karna hai.
'''
name = "Tops Technologies"
word3 = name.find("s",4,10)
print("After 4Th Position",word3)
#FIND INDEX 'S' 4 SE 10 TAK YANI 4 SE 9 TAK S KO FIND KARNA HAI 
'''
Index:   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Chars:   T o p s   T e c h n  o  l  o  g  i  e  s

'''
name = "Tops Technologies"
word4 = len(name)
print(f"Total Number Of String :{word4}")
print(len(name))
#Total Number Of Letter 


name = "Tops Technologies"
word5 = name.count("T")
print(f"Count {word5}")

word6 = name.count("TT")
print(f"Count {word6}")

#Total Number return Repeat letter