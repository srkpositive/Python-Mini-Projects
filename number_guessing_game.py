import random
randNo = random.randint(1, 100)
userGuess = None
guesses = 0

while(userGuess != randNo):
    userGuess = int(input("Enter your guess: "))
    guesses += 1
    if(userGuess == randNo):
        print("You guessed the right number!")
    elif(userGuess > randNo):
        print("You guessed it wrong!\nPlease enter smaller number.")
    else:
        print("You guessed it wrong!\nPlease enter larger number.")

print(f"You guessed the right number in {guesses} guesses.")
with open('highscore.txt') as f:
    high_score = int(f.read())

if(guesses<high_score):
    print("Congratulations!\nYou've broken the high score.")
    with open('highscore.txt', 'w') as f:
        f.write(str(guesses))