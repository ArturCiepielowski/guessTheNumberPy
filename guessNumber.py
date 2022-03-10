import random
print("Welcome to the Number Guessing Game!\nI am thinking of number between 1 and 100.")
dificultyChoice = input("Choose dificlty. Type 'easy' or 'hard': ")


def dificulty():
    if dificultyChoice == "easy":
        return 10
    elif dificultyChoice == "hard":
        return 5    



game = True

while game :
    print("Game continues")

