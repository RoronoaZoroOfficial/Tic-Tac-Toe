# X-O Game in Python

# Define the board as a list with 9 empty spaces
board = [" " for _ in range(9)]

# Function to print the board
def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

# Function to check for a win
def check_winner(player):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Function to check if the board is full (tie game)
def is_board_full():
    return " " not in board

# Main game loop
def play_game():
    current_player = "X"
    while True:
        print_board()
        try:
            move = int(input(f"Player {current_player}, enter a position (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid position! Please choose a number between 1 and 9.")
                continue
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")
            continue
        
        # Validate the move
        if board[move] == " ":
            board[move] = current_player
        else:
            print("This spot is already taken. Try again.")
            continue
        
        # Check for a win
        if check_winner(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break
        
        # Check for a tie
        if is_board_full():
            print_board()
            print("It's a tie!")
            break
        
        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()
