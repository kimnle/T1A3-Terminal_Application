# # Import
# import random
# from pick import pick

# # Function: start screen
# def start_screen():
#     print("""
#         _____    _     _    _____    _____    _____      ______    _    _    _____          _    _
#        /  ___|  | |   | |  |  ___|  /  ___|  /  ___|    |__  __|  | |  | |  |  ___|      __| |__| |__
#       |  /___   | |   | |  | |__   |  |___  |  |___       |  |    | |__| |  | |__       |__   __   __|
#       | ||_  |  | |   | |  |  __|   \___  \  \___  \      |  |    |  __  |  |  __|       __| |__| |__
#       |  \_| |  | \___/ |  | |___    ___|  |  ___|  |     |  |    | |  | |  | |___      |__   __   __|
#        \_____|   \_____/   |_____|  |_____/  |_____/      |__|    |_|  |_|  |_____|        |_|  |_|
#     """)
#     start_screen.player_name = input("What's your name?\n")
#     start_screen_options = ["Play", "Rules", "Scores", "Quit"]
#     start_screen_option, index = pick(start_screen_options)

# # Function: player chooses difficulty after selecting play
# def difficulty_level():
#     difficulty_level_options = ["Easy", "Medium", "Hard"]
#     difficulty_level_option, index = pick(difficulty_level_options)
#     if difficulty_level_option == "Easy":
#         difficulty_level.max_range = 10
#         difficulty_level.attempts = 5
#     elif difficulty_level_option == "Medium":
#         difficulty_level.max_range = 100
#         difficulty_level.attempts = 10
#     else:
#         difficulty_level.max_range = 1000
#         difficulty_level.attempts = 15

# # Function: generate random number
# def random_number():
#     random_number.number = random.randint(1, difficulty_level.max_range)

# # Function: takes player's guess
# def take_guess():
#     for take_guess.n in range(difficulty_level.attempts):
#         while True:
#             try:
#                 take_guess.player_guess = int(input(f"Guess a number between 1 and {difficulty_level.max_range}\n"))
#                 if 1 <= take_guess.player_guess <= difficulty_level.max_range:
#                     return take_guess.player_guess
#                 else:
#                     print("Please enter a number between the specified range")
#             except ValueError:
#                 print("Please enter a number")

# # Function: verifies player's guess
# def verify_guess(player_guess, number):
#     while True:
#         if take_guess.player_guess < take_guess.n:
#             return "Your guess is too low"
#         elif take_guess.player_guess > take_guess.n:
#             return "Your guess is too high"
#         else:
#             return "You guessed right!!"
#             break

# # Function: plays game
# def lets_play():
#     attempts = 0
#     win = False
#     while attempts < difficulty_level.attempts:
#         attempts += 1
#         player_guess = take_guess()
#         number = random_number()
#         answer = verify_guess(player_guess, number)
        
#         if answer == "You guessed right!!":
#             print(f"Congratulations, you guessed the random number {random_number.number} in {attempts} attempts!!")
#             win = True
#             break
#         else:
#             print("Try again!!")

#         if not win:
#             print(f"Sorry you ran out of attempts, the random number was {random_number.number}")