# Import
import random

# Function: player chooses difficulty
def choose_difficulty():
    print("Choose your difficulty")
    print("Easy")
    print("Medium")
    print("Hard")

    while True:
        try:
            difficulty = input("").lower()
            if difficulty != "easy" or "medium" or "hard":
                print("Please enter one of the three difficulties")
                continue
            break
            except ValueError:
                print("Please enter one of the three difficulties")

    if difficulty == "easy":
        attempts = 5
    elif difficulty = "medium":
        attempts = 10
    else:
        attempts = 15

    return attempts

def calc_score():
    points_lost = number - guess
    points_won = points_won - points_lost
    return points_won



# #Import
# import game

# if __name__ == "__main__":
#     game.start_screen()
#     game.difficulty_level()
#     game.random_number()
#     game.take_guess()
#     game.verify_guess()
#     game.lets_play()