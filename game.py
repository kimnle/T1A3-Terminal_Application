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
    player_name = input("What's your name?\n")
    options = ["Play", "Rules", "Scores", "Quit"]
    option, index = pick(options)
    return option

# Function: player chooses difficulty after selecting play
def difficulty():
    difficulty_options = ["Easy", "Medium", "Hard"]
    difficulty_option, index = pick(difficulty_options)
    if difficulty_option == "Easy":
        range = 10
        attempts = 5
    elif difficulty_option == "Medium":
        range = 100
        attempts = 10
    else:
        range = 1000
        attempts = 15
    
