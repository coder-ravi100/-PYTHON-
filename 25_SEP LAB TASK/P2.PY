#ALL LOGIC BUILDING PROGRAM IN ONE SET 

print("1.Count total even/odd digits from number")
print("2.REVERSE NUMBER")
print("3.FIND DIGITS NUMBER")
print("4.PALINDROME NUMBER")
print("5.ARMSTRONG NUMBER") 
print("6.STRONG NUMBER") 
print("7.PRIME NUMBER")
print("8.FIBONACCI NUMBER")
print("9.PERFECT NUMBER")
print("10.FACTORIAL NUMBER")
print("11.EXIT")

choice = int(input("ENTER THE CHOICE :"))

match choice:
    case 1:
        pass
    
    case 2:
        num = int(input("Enter The Number :"))
        rev = 0
        while num != 0:
            rem = num % 10
            rev = rev * 10 + rem
            num = num // 10
        print(f"== Reverse Number Is : {rev} ==")
    
    case 3:
        num = int(input("ENTER THE NUMBER :"))
        digits = 0
        while num != 0:
            num = num // 10
            digits += 1
        print(f"== Digits : {digits} ==")
    
    case 4:
        num = int(input("ENTER THE NUMBER :"))
        rev = 0
        temp = num
        while num != 0:
            rem = num % 10
            rev = (rev * 10) + rem
            num = num // 10
        if rev == temp:
            print(f"== PALINDROME NUMBER : {temp} ==")
        else:
            print(f"== NOT PALINDROME NUMBER : {temp} ==")
    case 5:
        pass

    case 6:
        pass

    case 7:
        pass

    case 8:
        pass

    case 9:
        pass

    case 10:
        pass
    case 11:
        print("Exiting Program...")


