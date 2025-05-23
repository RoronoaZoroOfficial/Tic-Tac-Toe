import tkinter as tk
from tkinter import messagebox

# Initialize main window
window = tk.Tk()
window.title("Yash Dabas Game")
window.geometry("300x350")

# Game state
board = [" " for _ in range(9)]
current_player = "X"

# Function to update the game board visually
def update_board():
    for i, cell in enumerate(board):
        buttons[i].config(text=cell)

# Function to check for a winner
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

# Function to check if the board is full
def is_board_full():
    return " " not in board

# Function to handle a player's move
def make_move(index):
    global current_player
    if board[index] == " ":
        board[index] = current_player
        update_board()
        
        # Check for win or tie
        if check_winner(current_player):
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_game()
        elif is_board_full():
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_game()
        else:
            # Switch player
            current_player = "O" if current_player == "X" else "X"
    else:
        messagebox.showwarning("Invalid Move", "This spot is already taken!")

# Function to reset the game
def reset_game():
    global board, current_player
    board = [" " for _ in range(9)]
    current_player = "X"
    update_board()

# Set up buttons for each cell on the board
buttons = []
for i in range(9):
    button = tk.Button(window, text=" ", font=('Arial', 24), width=5, height=2,
                       command=lambda i=i: make_move(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Reset button
reset_button = tk.Button(window, text="Reset", font=('Arial', 16), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3)

# Run the main loop
window.mainloop()
