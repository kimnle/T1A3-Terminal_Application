# Import
import random
from pick import pick

# Function: start screen
def start():
    print("""
        _____    _     _    _____    _____    _____      ______    _    _    _____          _    _
       /  ___|  | |   | |  |  ___|  /  ___|  /  ___|    |__  __|  | |  | |  |  ___|      __| |__| |__
      |  /___   | |   | |  | |__   |  |___  |  |___       |  |    | |__| |  | |__       |__   __   __|
      | ||_  |  | |   | |  |  __|   \___  \  \___  \      |  |    |  __  |  |  __|       __| |__| |__
      |  \_| |  | \___/ |  | |___    ___|  |  ___|  |     |  |    | |  | |  | |___      |__   __   __|
       \_____|   \_____/   |_____|  |_____/  |_____/      |__|    |_|  |_|  |_____|        |_|  |_|
    """)
    start.player_name = input("What's your name?\n")
    start_options = ["Play", "Rules", "Scores", "Quit"]
    start_option, index = pick(start_options)

# Function: player chooses difficulty after selecting play
def difficulty():
    difficulty_options = ["Easy", "Medium", "Hard"]
    difficulty_option, index = pick(difficulty_options)
    if difficulty_option == "Easy":
        difficulty.max_range = 10
        difficulty.attempts = 5
    elif difficulty_option == "Medium":
        difficulty.max_range = 100
        difficulty.attempts = 10
    else:
        difficulty.max_range = 1000
        difficulty.attempts = 15

# Function: get player's guess
def guess():
    for n in range(difficulty.attempts):
        while True:
            try:
                player_guess = int(input(f"Guess a number between 1 and {difficulty.max_range}\n"))
                if 1 <= player_guess <= difficulty.max_range:
                    return player_guess
                else:
                    print("Please enter a number between the specified range")
            except ValueError:
                print("Please enter a number")