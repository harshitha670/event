import random

print("Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 100.")

# Random number between 1 and 100
number_to_guess = random.randint(1, 100)
attempts = 0
guessed = False

while not guessed:
    guess = input("Enter your guess: ")
    
    # Check if input is a number
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
        guessed = True
