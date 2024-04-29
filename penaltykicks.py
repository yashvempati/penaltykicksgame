import random

def play_penalty_shootout():
    print("Welcome to the penalty shootout!")
    print("Score a goal to win (!)")

    player_name = input("What is your name? ")
    print(f"\n{player_name}, can you beat the keeper?")
    print("\n ◯")
    print(" |_|")

    keeper_position = random.randint(1, 3)
    valid_input = False
    while not valid_input:
        guessed_position = input("Will you go left (1), right (3) or down the middle (2)? ")
        if guessed_position in ['1', '2', '3']:
            valid_input = True
            break
        else:
            print("Invalid input. Please enter 1, 2 or 3.")

    if int(guessed_position) != keeper_position:
        print("\n'Oh, wonderful! What a goal! And what a time, in what a place! What a player!'- Peter Drury")
    else:
        print("\n'The end. The end. Make sense of that. Where on Earth are we now? A night of dismay.'- Peter Drury.")

    print("\nThanks for playing!")

if __name__ == "__main__":
    play_penalty_shootout()
