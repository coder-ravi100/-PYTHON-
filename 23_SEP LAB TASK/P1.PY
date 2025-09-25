# name = "Ravi"
# reverse_name = name[::-1]
# print(reverse_name)

word = "Ravi"
temp = word
word = word[-1] + word[1:-1] + word[0]
print(f"Original String :{temp}")
print(f"Reverse String :{word}")
#output : ivaR

print("\n")

word = "Abhijit"
temp = word
word = word[-1] + word[1:-1] + word[0]
print(f"Original String :{temp}")
print(f"Reverse String :{word}")
#output = tbhijiA

word = "Abhijit"
word = word[1] + word[-1]
print(word)
#output : ai
#output : bii

