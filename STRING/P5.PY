#SPLIT METHOD
#JOIN()FUNCTION

#1.SPLIT EK STRING METHOD HAI JO STRING KO TODKAR EK LIST BANA DETA HAI
#EX 1:
text = "I Love Python Programming"
word = text.split()
print(word)

#EX 2:
fruits = "apple,mango,banana,grapes"
backet = fruits.split(",")
print(backet)

#EX 3:
message = "one,two,three,four,five"
part = message.split(" ",2)
print(part)

#EX 4:
name ="Tops Technologies"
lst = name.split("t")
print(f"Split  By t {lst}")


sentence = "This Is My Python Class And It Will Complete  by 10"
print(len(sentence))#COUNTING NUMBER OF LETTER FROM STRING
lst2 = sentence.split()
print(f"No Of Words ==={len(lst2)}")#COUNTING NUMBER OF WORDS FROM STRIMG


#2.JOIN()FUNCTION
#JOIN () EK STRING METHOD HAI JO LIST(YA ITERABLE) KE ELEMENTS KO JODKAR EK SINGLE STRING BANA DETA HAI
#SYNTEX 
#"SEPERATER".JOIN(ITERABLE)
#separator → jodne ke beech kya lagana hai (space, comma, dash, etc.)
#iterable → list, tuple, ya string ke sequence.

#EX 1:(SPACE KE SATH JOIN)
words = ['I','Love','Python']
sentence = " ".join(words)
print(sentence)

#EX 2:(COMMA KE SATH JOIN)
fruits = ["apple" , "Mango", "Banana"]
result = ",".join(fruits)
print(result)

#EX 3:(DASH KE SATH JOIN)
nums = ["10","20","30"]
result = "_".join(nums)
print(result)


#EX 4: JOIN ()FUNCTION
lst3 = ["Apple","Banana","Cherry"]
fruits = " ".join(lst3)
print(fruits)
fruits = "*".join(lst3)
print(fruits)