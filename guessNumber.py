import random
print("Welcome to the Number Guessing Game!\nI am thinking of number between 1 and 100.")
dificultyChoice = input("Choose dificlty. Type 'easy' or 'hard': ")
number = random.randint(1,100)

def dificulty():
    if dificultyChoice == "easy":
        return 10
    elif dificultyChoice == "hard":
        return 5    



game = True
lifes= dificulty()
while game :

    print(f"You have {lifes} attempts remaining to guess the number. ")
    guess=int(input("Make a guess: "))
    
    if guess == number :
        print("You have won ")
        game = False
    elif guess > number:
        print("Too high try lower")
    elif guess < number:
        print("Too low try higher")     
    
    lifes = lifes -1
    if lifes == 0 :
        print("Game Over")
        game = False



