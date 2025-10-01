#1.ISDIGIT()FUNCTION
#2.ISALPHA()FUNCTION
#3.ISANUM()FUNCTION
#4.ENDSWITH()FUNCTION

#1.ISDIGIT()FUNCTION
#CHECK KARTA HAI KI STRING KE SAARE CHARACTER DIGIT(0-9)HAI YAH NAHI
#AGAR SABHI DIGITS HAIN TO TRUE WORNA FALSE RETURN KAREGA
s1 = "12345"
s2 = "12a45"
s3 = "acb"
s4 = "123 45"
s5 = "123@123"

print(f"{s1.isdigit()}")
print(f"{s2.isdigit()}")
print(f"{s3.isdigit()}")
print(f"{s4.isdigit()}")
print(f"{s5.isdigit()}")

print("-------")
#2.ISALPHA FUNCTION
#CHECK KARTA HAI KI STRING KE SAARE CHARACTERS ALPHABETS (A-Z OR a-z,0-9) HAIN YAH NAHI
#AGAR SABHI LETTERS HAIN TO TRUE RETURN KAREGA OTHERWISE FALSE RETURN KAREGA
s1 = "PYTHON"
s2 = "python"
s3 = "PY1020"
s4 = "py1020"
s5 = "pyhthon@"
s6 = "Pyth on"

print(f"{s1.isalpha()}")
print(f"{s2.isalpha()}")
print(f"{s3.isalpha()}")
print(f"{s4.isalpha()}")
print(f"{s5.isalpha()}")
print(f"{s6.isalpha()}")

print("------")
#3.ISALNUM()FUNCTION
#CHECK KARTA HAIN KI STRING KE SAARE CHARECTERS ALPHABETS YA DIGIT (DONO ALLOWED) HAIN
#AGAR SPECIAL CHARACTERS (SPACE @ & ETC) AAYEGE TO FALSE HOGE

s1 = "python123"
s2 = "python"
s3 = "12345"
s4 = "Hello@123"
s5 = "Hello 123"

print(f"{s1.isalnum()}")
print(f"{s2.isalnum()}")
print(f"{s3.isalnum()}")
print(f"{s4.isalnum()}")
print(f"{s5.isalnum()}")


#ENDSWITH()FUNCTION
#STRING ENDSWITH FUNCTION CHECK KARTA HAI KI STRING KE END  DIE HUE VALUE HAI YAH NAHI
#AGAR MATCH KARTA HAI-->TRUE RETURN KAREGA
#AGAR MATCH NAHI KARTA TO -->FALSE RETURN KAREGA


print("------")
#EX 1: ENDSWITH()
message = "Have a good day"
print(message.endswith("test"))
print(message.endswith("day"))
print(message.endswith("goods"))

#EX 2: ENDSWITH()
email = input ("Enter The Email ID:")
ans = email.endswith(".com")

if ans:
    print(f"{email}:is Valid Email Address")
else:
    print(f"{email}:is Invalid Email Address")
