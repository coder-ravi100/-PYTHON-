#REPLACE() STRING FUNCTION
#✅OLD - JO PART/SUBSTRING REPLACE KARNA HAI
#✅NEW - JO NAYA TEXT DALNA HAI
#✅COUNT - (OPTIONAL) KITNI BAAR REPLACE KARNA HAI AGAR NAHI LIKHA TO SAARE
'''
REPLACE HO JATE HAIN
'''
#✅ Example 1: Simple replace
name = "Tops Technilogies"
new_name = name.replace("Tops","My")
print(new_name)

#✅ Example 2: Multiple replace
sentence = "Python Is Easy, Python Is Powerful"
result = sentence.replace("Python","C++")
print(result)

#✅ Example 3: Replace with count
text = "apple  apple apple"
new_text = text.replace("apple","Orange",2)
print(new_text)

#✅ Example 4: Replace character
word = "banana"
change = word.replace("a","o")
print(change)

'''
3. Important Point
replace() nayi string return karta hai.
Original string change nahi hoti (kyunki Python me strings immutable hote hain).
'''
sentence1 = input ("Enter Senetence :")
print(f"{sentence1} Original")
word = input ("Enter Word To Replace :")
new_word = input ("Enter The New Word To Replace :")
sentence1 = sentence1.replace(word,new_word)
print(f"{sentence1} Original")