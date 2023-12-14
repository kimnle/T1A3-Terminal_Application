import random

def game_intro():
    print("Welcome to the Number Guessing Game!")
    player_name = input("What's your name?\n")
    difficulty = input(f"Hey {player_name}, choose your difficulty level. Easy, medium or hard?\n")

game_intro()