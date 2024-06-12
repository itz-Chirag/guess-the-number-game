import random

# Function to generate a random number within the specified range and give a hint
def random_num(min_val, max_val, diff_choosed):
    to_guess = random.randint(min_val, max_val)
    hint(to_guess, diff_choosed)

# Function to introduce the game rules and start the game
def intro(a=1):
    print("Welcome To Guess The Number Game")
    print("Simple Rules-\n•You Will Have To Guess The Number In 7 Tries")
    print("•TOO LOW/HIGH - The Number To Guess Is 50-200 More/Less Than Your Guess")
    print("•LOW/HIGH - The Number To Guess is 10-50 More/Less Than Your Guess")
    print("•Close And HIGH/LOW - The Number To Guess is 1-10 More/Less Than Your Guess")
    difficulty() 

# Function to choose the difficulty level
def difficulty(a=1):
    print("Choose Difficulty")
    print("1. Easy(0-50)\n2. Medium(0-100)\n3. Hard(0-200)")
    diff_choosed = int(input("Your Choice: "))
    try:
        if diff_choosed == 1:
            random_num(0, 50, 1)
        elif diff_choosed == 2:
            random_num(0, 100, 2)
        elif diff_choosed == 3:
            random_num(0, 200, 3)
    except ValueError:
        print("Please Input Valid Value")

# Function to give a hint about the number being even or odd
def hint(to_guess, diff_choosed):
    print("Before You Start, A Hint For You..")
    if to_guess % 2 == 0:
        print("The Number Is Even")
    else:
        print("The Number Is Odd")
    guess(to_guess, diff_choosed)

# Variables to track attempts and guess history
attempts = [7]
guess_history = []

# Function to handle the guessing process
def guess(to_guess, diff_choosed):
    while sum(attempts) >= 0:
        user_guess = int(input("Your Guess:  "))
        guess_history.append(user_guess)
        attempts.append(-1)
        print("You Have ", sum(attempts), " Attempts Left")
        guess_checker(to_guess, user_guess, diff_choosed)
    print("You Don't Have Any Attempt Left")
    outro1(to_guess, diff_choosed)

# Function to check the guess against the target number
def guess_checker(to_guess, user_guess, diff_choosed):
    difference = user_guess - to_guess
    if 200 >= difference >= 50:
        print("TOO HIGH")
        guess(to_guess, diff_choosed)
    elif 50 > difference > 10:
        print("HIGH")
        guess(to_guess, diff_choosed)
    elif 10 >= difference >= 1:
        print("Close And High")
        guess(to_guess, diff_choosed)
    elif -10 <= difference <= (-1):
        print("Close But Low")
        guess(to_guess, diff_choosed)
    elif -50 < difference < (-10):
        print("LOW")
        guess(to_guess, diff_choosed)
    elif -200 <= difference <= (-50):
        print("TOO LOW")
        guess(to_guess, diff_choosed)
    elif difference == 0:
        print("You WON")
        outro2(to_guess, diff_choosed)

# Function for the end of the game if the player didn't guess the number
def outro1(to_guess, diff_choosed):
    print("You Couldn't Guess The Number\nThe Number Was ", to_guess)
    print("The Guesses You Made", guess_history)

# Variables to track scores for different difficulty levels
score_easy = []
score_medium = []
score_hard = []

# Function to handle scoring and ask if the player wants to play again
def score(diff_choosed):
    if diff_choosed == 1:
        score_easy.append(10)
        print("Your Score\nEasy:", sum(score_easy))
    elif diff_choosed == 2:
        score_medium.append(10)
        print("Your Score\nMedium:", sum(score_medium))
    elif diff_choosed == 3:
        score_hard.append(10)
        print("Your Score\nHard:", sum(score_hard))
    play_again = str(input("Do You Want To Play Again? (Yes/No): "))
    try:
        if play_again.upper() == "YES":
            print("5 More Attempts Added")
            attempts.append(4)
            intro()
        elif play_again.upper() == "NO":
            print("Your Score\nEasy:", sum(score_easy), "\nMedium:", sum(score_medium), "\nHard:", sum(score_hard))
            print("Have A Nice Day")
    except ValueError:
        print("Please Input Valid Value")
        
# Function for the end of the game if the player guessed the number
def outro2(to_guess, diff_choosed):
    print("You Guessed It!!")
    score(diff_choosed)

# Start the game
intro()
