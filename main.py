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
        min_range = 1
        max_range = 10
    elif difficulty = "medium":
        attempts = 10
        min_range = 1
        max_range = 100
    else:
        attempts = 15
        min_range = 1
        max_range = 1000

    return attempts

# # Function: calculates score
# def calc_score(current_points, number_to_be_guessed, current_guess):
#     points_lost = number_to_be_guessed - current_guess
#     current_points = abs(current_points - points_lost)
#     return current_points

# Function: saves scores
def save_scores():
    try:
        with open("scores.txt", "r") as scores_file:
            scores = scores_file.read()
    except FileNotFoundError:
        print(f"Play to add your scores!")

    with open("scores.txt", "a") as scores_files:
        scores_files.write(f"{difficulty} difficulty - you guessed the number in {attempts} attempts\n")

def play_game(attempts, min_range, max_range):
    number_to_be_guessed = random.randint(min_range, max_range)
    
    for round in range(1, attempts + 1):
        print(f"Attempt {round} out of {attempts}")

# #Import
# import game

# if __name__ == "__main__":
#     game.start_screen()
#     game.difficulty_level()
#     game.random_number()
#     game.take_guess()
#     game.verify_guess()
#     game.lets_play()