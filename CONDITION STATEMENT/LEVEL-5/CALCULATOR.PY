# SIMPLE CALCULATOR USING match-case

num1 = int(input("Enter The Number 1 : "))
num2 = int(input("Enter The Number 2 : "))
n1 = float (num1)
n2 = float (num2)
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Remainder")
print("6. Exit")

operator = input("Enter The Choice: ")

match operator:
    case '1':
        print(f"Addition is : {num1 + num2}")

    case '2':
        print(f"Subtraction is : {num1 - num2}")

    case '3':
        print(f"Multiplication is : {num1 * num2}")

    case '4':
        if (num2 != 0):
            print(f"Division is : {num1 / num2}")
        else:
            print("Error! Division by zero")

    case '5':
        print(f"Remainder is : {n1 % n2}")

    case '6':
        print("Exiting... Goodbye!")

    case _:
        print("Invalid choice! Please select from 1 to 6.")
