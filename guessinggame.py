import random

def main():
    counter = 0

    print("Give range of random number!\n")

    upper = int(input("Upper Bound: "))
    lower = int(input("Lower Bound: "))

    number = random.randint(lower, upper)

    print(f"Guess the random number between {lower} and {upper}!\n")

    max_attempts = 5

    while (counter < max_attempts):
        counter += 1
        guess = int(input("Enter guess: "))

        if guess < number:
            print("Go higher!\n")
        elif guess > number:
            print("Go lower!\n")
        elif guess == number:
            print(f"Correct! Number was {number}. You guessed in {counter} tries.")
            return

    print(f"Game over. The number was {number}. Better luck next time!")

if __name__ == "__main__":
    main()
