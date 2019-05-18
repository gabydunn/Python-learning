#Create a game that asks the player to guess a random number between 1 and 20
#Player gets 6 guesses
import random
print('Hello, what is your name?')
name = input().title()
#The number the player is trying to guess. randint is inclusive of the range it's given
secretNumber = random.randint(1,20)
print(f"Well {name}, I'm thinking of a number between 1 and 20.")
#go up to, but including 7
for guessesTaken in range(1,7):
    print('Take a guess:')
    try:
        guess = int(input())
        if guess > secretNumber:
            print("You guessed too high!")
        elif guess< secretNumber:
            print("You guessed too low!")
        else:
            break #if the guess is correct
    except ValueError:
        print('Please enter a number between 1 and 20')
if guess == secretNumber:
    print(f"Good job {name}! You guessed {str(guessesTaken)} time(s)")
else:
    print(f"Nope! You're all out of guesses. The number I was thinking of was {secretNumber}")