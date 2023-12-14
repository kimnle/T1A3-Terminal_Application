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