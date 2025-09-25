'''
ENDSWITH () FUNCTION :
STRING.ENDWITH("TEXT") CHECK KARTA HAI KI STRING  KE END DIE HUE VALUE HAI YAH NAHI
AGAR MATCH KARTA HAI ->TRUE RETURN KAREGA
AGAR MATCH NAHI KARTA ->FALSE RETURN KAREGA
'''
message = "Have a good day!!!"
print(message.endswith("test"))
print(message.endswith("day!!!"))


email = input("Enter Email Id :")
ans = email.endswith(".com")

if ans:
    print(f"{email} is valid email address")
else:
    print(f"{email} is Invalid email address")



'''
practice set
📘 Practice Set - Functions & String Functions
Part A - Direct String Function Practice

1.Ek string input lo aur check karo:
kya wo .endswith("ing") karta hai?
kya wo .startswith("a") karta hai?

2.Ek string input lo aur .isalpha() use karke check karo ki sirf alphabets hain ya nahi.

2.Ek string input lo aur .isdigit() use karke check karo ki sirf digits hain ya nahi.

3.Ek string input lo aur .isalnum() check karo (sirf alphabets+numbers hone chahiye).

4.Ek string input lo aur .upper(), .lower(), .title() ka output print karo.

Part B - Small Programs (using functions)

1.Program banao jo input email le aur check kare:
.com se end hota hai ya nahi
Agar hota hai → "Valid email" print karo
Agar nahi → "Invalid email"

2.Program likho jo mobile number input le:
Check karo ki wo 10 digit ka hai (len(number) == 10)
Aur saare digits hai (.isdigit() == True)
Valid ho to print: "Valid Mobile Number"

3.Program likho jo password input le:
Kam se kam 8 character ka ho
.isalnum() true ho
Agar valid → "Password Accepted" print karo

4.Ek program likho jo string input le aur check kare ki usme vowel (a, e, i, o, u) hai ya nahi.
(hint: "a" in string use kar sakte ho).

5.Ek program likho jo sentence input le aur user se ek word input karwao.
.endswith() use karke check karo ki sentence us word se end hota hai ya nahi.

Part C - Custom Function Practice

Apna khud ka function banao check_email(email) jo return kare True/False based on .com check.

Apna function banao check_mobile(mobile) jo valid mobile number check kare.

Ek function banao count_vowels(word) jo return kare total vowels ka count.
'''