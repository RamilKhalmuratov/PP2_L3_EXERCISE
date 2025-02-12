import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    secret_number = random.randint(1, 20)
    
    while True:
        print("\nTake a guess.")
        try:
            guess = int(input())
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number.")
            break

guess_the_number()
