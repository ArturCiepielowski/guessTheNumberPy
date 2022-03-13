import random
print("Welcome to the Number Guessing Game!\nI am thinking of number between 1 and 100.")
dificultyChoice = input("Choose dificlty. Type 'easy' or 'hard': ")


def dificulty():
    if dificultyChoice == "easy":
        return 10
    elif dificultyChoice == "hard":
        return 5    



game = True
lifes= dificulty()
while game :

    print(f"You have {lifes} attempts remaining to guess the number. ")
    lifes = lifes -1
    if lifes == 0 :
        print("Game Over")
        game = False



