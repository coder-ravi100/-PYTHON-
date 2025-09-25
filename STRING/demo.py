# email = input("Enter Email ID: ")

# if "@" in email and "." in email:
#     if email.index("@") < email.rindex(".") and email.index("@") != 0 and email[-1] != ".":
#         print("Valid Email ID")
#     else:
#         print("Invalid Email ID")
# else:
#     print("Invalid Email ID")

text = input("Enter a string: ")
vowel_found = False

for ch in text:
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' \
       or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
        vowel_found = True
          

if vowel_found:
    print("Vowel Present in the string")
else:
    print("No Vowel in the string")





