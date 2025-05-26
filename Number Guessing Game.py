import random
print("Hi! Welcome to the number guessing game! I will be choosing a number from 1 to 30 and you have to guess it")
computer = random.randint(1, 30)
guesses = 5
print("You have 5 guesses to guess the number I'm thinking of. Choose wisely!")
if computer%2 == 0:
    print("The number I am thinking of is even")
else:
    print("The number I am thinking of is odd")
while guesses > 0:
    guess = int(input("Enter your guess :\n"))
    guesses = guesses - 1
    if guesses == 0:
        print("You are out of guesses!")
        break
    if computer > guess:
        print("You are too low! Try again!")
    if computer < guess:
        print("You are too high! Try again!")
    if computer == guess:
        print("Congratulations!! You guessed it right! You won!! You guessed it in", guesses,"tries!")
        break