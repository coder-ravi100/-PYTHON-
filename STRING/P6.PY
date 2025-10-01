#1.STRIP() FUNCTION HAI
#STRING KE STARTING AND ENDING KE SPACES (YA DIYA GAYA CHARACTERS) KO REMOVE KARTA HAI
#BEECH KE SPACES KO REMOVE NAHI KARTA

#1.NORMAL SPACE REMOVE
msg = "Hello World"
print(msg.strip())

#2.SPECIFIC CHARACTER REMOVIE
word = "xxxPythonxxx"
print(word.strip("x"))

#3.STIRP()
name = "Tops Technologies"
print(len(name))
name = name.strip()
print(len(name))

print(sorted(name))
#2.SORT  FUNCTION HAI
#LIST KE ELEMENTS KO ASCENDING ORDER(DEFUALT) ME ARRAGE KARTA HAI
#SIRF LIST PE KAAM KARTA HAI (STRING PE NAHI)
#ORIGINAL LIST KO HI CHANGE KAR DEAT HAI(IN-PLACE)

#1.NUMBERS SORTING
nums = [12,45,67,34]
nums.sort()
print(nums)


#2.REVERSE SORTING
nums = [12,45,2,67,34]
nums.sort(reverse=True)
print(nums)

#3.STRING SORTING
cities = ["surat","ahmedabad","rajkot","baroda"]
cities.sort()
print(cities)


#4.SORT FUNCTION()
#WORDS TO BE SORTED FROM SENTENCE
sentence = "This is Tuesday"
lst = sentence.split()
sort_lst = sorted(lst)
print(f"Original list {lst} and sorted list {sort_lst}")

sort_list_len = sorted(lst,key = len)
print(f"Original List {lst} and sorted list {sort_list_len}")