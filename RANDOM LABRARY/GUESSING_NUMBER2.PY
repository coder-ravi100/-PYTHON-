#NUMBER GUESSING GAME
import random

attempt = 5
i = 1
num = random.randint(1, 100)

print("-------------------------------")
print("Welcome To Number Guessing Game")
print("-------------------------------")
print("Rules:")
print("Guess The  Number Between 1 to 100")
print(f"You Have Attempts To Find The Number: {attempt}")
print("Let's Begin !")
print("***************************************")
while i <= attempt:
    guess_num = int(input("\nPlease Guess Number : "))

    if num > guess_num:
        print("TOO LOW !")
    elif num < guess_num:
        print("TOO HIGH !")
    else:
        print("Congratulation! You have guessed the correct number.")
        break

    if i < attempt:
        print(f"Attempts Left : [{attempt - i}]")
    else:
        print("Game Over! You have used all attempts.")
        print(f"The Correct Number was : [{num}]")
    i += 1
