'''
1️⃣ split() function
🔹 Kya karta hai?

String ko chhote-chhote parts (list) me tod deta hai
Usually space ya koi delimiter ke basis pe todta hai

🔹 Syntax:
string.split(separator, maxsplit)
'''
#Example 1: Simple split by space
text = "Romil Is a Good Boy"
words = text.split()
print(words)

#Example 2: Split by comma
data = "apple,banana,orange"
fruits = data.split(",")
print(fruits)

#Example 3: Split with maxsplit
text = "I Love Python Programming"
words = text.split(" ",2)
print(words)
#Sirf 2 baar split kiya, baaki sab last element me raha


'''
2️⃣ join() function
🔹 Kya karta hai?

List ke elements ko ek string me jod deta hai
Jo separator hum specify karenge, usse join karta hai

🔹 Syntax:
separator.join(list_of_strings)
separator → string ke beech me kya lagana hai (space, comma, dash…)
'''
#Example 1: Join with space
words = ['Abhi','is','Good']
sentence = " ".join(words)
print(sentence)

#Example 2: Join with comma
fruits = ['apple','banana','orange']
result = ",".join(fruits)
print(result)

#3️⃣ Split + Join ka combo
#Often split ke baad manipulate kar ke join karte hain
text = "Python is easy"
words = text.split()
words.reverse()
new_text = "_".join(words)

print(f"Normal Case:{text}")
print(f"Reverse Case:{new_text}")

print("\n")#OTHER EXAMPLE
name = "Tops Technologies pvt ltd"
lst = name.split()
print(lst)

lst1 = name.split("t")
print(f"Split by t {lst1}")

sentence = "This is my python class and it will complete by 10"
print(len(sentence))
#


