'''
number gussing - random
'''
'''
25th Sep : 
 1. Convert into Uppercase
 2. Convert into Lowercase
 3. Find length
 4. Replace 
 5. Exit
Please enter your choice : 1
Please enter string that you want otconvert in Uppercase
qwert
QWERT
'''
while True:#while 1:
    print("1.CONVERT INTO UPPERCASE")
    print("2.CONVERT INTO LOWERCASE ")
    print("3.FIND LENGTH")
    print("4.REPLACE")
    print("5.EXIT")

    choice = int (input ("ENTER THE CHOICE :"))

    match choice:
        case 1:
            text = input("ENTER THE STRING :")
            word = text.upper()
            print(word)
        case 2:
            text = input("ENTER THE STRING :")
            word = text.lower()
            print(word)
        case 3:
            text = input("ENTER THE STRING :")
            print("TOTAL LENGTH :",len(text))
        case 4:
            text = input("ENTER THE STRING :")
            old_text = input ("ENTER THE STRIING YOU WANT TO REPLACE :")
            new_text = input ("ENTER THE NEW STRING THAT YOU WANT TO REPLACE :")
            print(f"AFTER REPLACE {text.replace(old_text,new_text)}")
        case 5:
            break
        case _:
            print("INVALID CHOICE..")
        

    
