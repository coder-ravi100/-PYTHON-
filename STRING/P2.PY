#5.FIND() FUNCTION 
#find function substring ka index number (position) return karta hai
#agar substring nahi mila to -1 return karta hai
name = "all girls are smart"
word_one = name.find("e") # 12
word_two = name.find("to") # -1
print(word_one)
print(word_two)

#OTHER EXAMPLE FIND FUNCTION
name = "all boy are cute"
word = name.find("o",4,10)
print(word)
'''
DRY RUN CODE
a l l   b o y   a r e    c  u  t  e
0 1 2 3 4 5 6 7 8 9 10   11 12 13 14
'''
#6.LENGHT() FUNCTION
#RETURN TOTAL NUMBER OF LETTER
name = "school is boring place"
print(len(name)) #22 space including

#7.COUNT() FUNCTION
#RETURN OF REPEAT CHARACTER
name = "girls are crezy 🤣"
word = name.count("e")
print(word)

name = "girls are crezy and boys are crezy 🤣"
word = name.count("crezy")
print(word)

#8.REPLACE FUNCTION()
#REPLACE THE WORD OR LETTER
name = "Tops Technologies"
new_word = name.replace("Tops","science")
print(new_word)

#REPLACE MULTIPLY PLACE
sentance = "python is a crezy language, python is dumbed language"
result = sentance.replace("python","C++")
print(result)

#REPLACE WITH COUNT 
text = "apple apple apple"
new_word = text.replace("apple","banana",2)
print(new_word)

#REPLACE  CHARACTER
word = "banana"
new_text = word.replace("a","o")
print(new_text)

#INPUT WISE PROGRAM
word1 = input ("Enter The Word :")
print(f"{word1}")
word2 = input ("Enter The Word To Replace :")
word3 = input ("Enter The New Word :")
word4 = word1.replace(word2,word3)
print(f"{word4}")





