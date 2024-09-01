import random

# Define valid moves and their relationships
MOVES = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
WINNING_COMBINATIONS = {'r': 's', 'p': 'r', 's': 'p'}

# Start the game
user = input("What's your choice? 'r' for Rock, 'p' for Paper, and 's' for Scissors\n").lower()

# Check if the user entered a valid move
if user not in MOVES:
    print("Invalid entry. Please enter 'r' for Rock, 'p' for Paper, or 's' for Scissors.")
else:
    pc = random.choice(list(MOVES.keys()))

    # Display the player and PC moves
    print(f"User played: {MOVES[user]}")  # Display the full move name using the MOVES dictionary
    print(f"PC played: {MOVES[pc]}")  # Display the full move name using the MOVES dictionary

    # Check the game result
    if user == pc:
        # Tie condition
        print("It's a tie!")
    elif pc == WINNING_COMBINATIONS[user]:
        # User won condition
        print("You won!")
    else:
        # PC won condition
        print("You lose!")
