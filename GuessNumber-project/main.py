#Computer generates random number and player guess a number, if number matches player wins
#Player playes until he loses, how many times he wins makes a high-score
#Compares with files hi-score saved to figure out best-score

import random

computerGuess = random.randint(1,20) #randint gives number between two numbers
playerGuess = int(input("Enter your guess between 1 to 20: "))
wins = 0
loss = 0

print(f"Your Guess: {playerGuess}, Computer Guess: {computerGuess}")

if(playerGuess == computerGuess):
    wins += 1
    print("You won")
else:
    loss += 1
    print("You lose")
