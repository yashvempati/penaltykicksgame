## I hate Pylint very much
import random

print("Welcome to the penalty shootout!")  
print("Score a goal to win (!)")

player_name = input("What is your name? ")  

print(f"{player_name}, can you beat the keeper?")  
print(" ◯")
print("|_|")

game_on = True
while game_on:
    keeper_position = random.randint(1, 3)
    guessed_position = input("Will you go left (1), right (3) or down the middle (2)? ")

    if guessed_position != keeper_position:
        print("'Oh, wonderful! What a goal! And what a time, in what a place! What a player!'- Peter Drury")
        game_on = False  ## End game because like a goal was scored yeah?
    else:
        print("'The end. The end. Make sense of that. Where on Earth are we now? A night of dismay.'- Peter Drury.")
        game_on = False  ## Still end game, you don't get retries

## Print this line after the game loop finishes
print("Thanks for playing! Ab chal jake padhai kar")