import random

print("Welcome to the Number Guessing Game")
print("I'm thinking of a number betweeen 1 and 100")

numbers = list(range(1,101))

difficulty = input("Choose your difficulty type hard or easy")
number = random.choice(numbers)

def guess():
    if difficulty == "hard":
        for attempts in range(1,6):
            number1 = int(input("Make a guess:"))
            if number1 < number:
                print("Too low")
                print(f"You have {5 - attempts} guesses left")
                if 5 - attempts == 0:
                    print(f"Game over. Number was {number}")
            elif number1 > number:
                print("Too high")
                print(f"You have {5 - attempts} guesses left")
                if 5 - attempts == 0:
                    print(f"Game over. Number was {number}")
            else :
                number == number1
                print("You guessed correctly")
                break
    else :
        for attempts in range(1, 11):
            number1 = int(input("Make a guess:"))
            if number1 < number:
                print("Too low")
                print(f"You have {10 - attempts} guesses left")
                if 10 - attempts == 0:
                    print(f"Game over. Number was {number}")

            elif number1 > number:
                print("Too high")
                print(f"You have {10 - attempts} guesses left")
                if 10 - attempts == 0:
                    print(f"Game over. Number was {number}")

            else:
                number == number1
                print("You guessed correctly")
                break
guess()