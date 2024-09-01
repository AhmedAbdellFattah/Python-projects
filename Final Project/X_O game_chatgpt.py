import tkinter as tk
import random
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")

        # Game variables
        self.board = [" " for _ in range(9)]
        self.playing = True
        self.user_wins, self.computer_wins, self.ties = 0, 0, 0

        # GUI elements
        self.score_label = tk.Label(master, text="You: 0 Computer: 0 Ties: 0", font=('Arial', 14))
        self.score_label.grid(row=0, column=0, columnspan=3)

        self.buttons = [tk.Button(master, text=" ", font=('Arial', 20), width=5, height=2, command=lambda j=j: self.click(j)) for j in range(9)]
        for i, button in enumerate(self.buttons):
            button.grid(row=i // 3 + 1, column=i % 3)

        self.restart_button = tk.Button(master, text="Restart", font=('Arial', 14), command=self.restart)
        self.restart_button.grid(row=4, column=1)

        # Initialize the game
        self.restart()

    def click(self, i):
        if self.playing and self.board[i] == " ":
            self.make_move("X", i)
            if self.playing:
                self.computer_turn()

    def computer_turn(self):
        winning_move = self.find_winning_move("O") or self.find_winning_move("X")

        if winning_move is not None:
            self.make_move("O", winning_move)
        else:
            self.make_random_move("O")

    def make_move(self, player, position):
        self.board[position] = player
        self.buttons[position].config(text=player)
        self.check_and_handle_result(player)

    def make_random_move(self, player):
        choices = [i for i in range(9) if self.board[i] == " "]
        if choices:
            self.make_move(player, random.choice(choices))

    def find_winning_move(self, player):
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = player
                if self.check_winner(player):
                    self.board[i] = " "  # Reset the board
                    return i
                self.board[i] = " "  # Reset the board
        return None

    def check_and_handle_result(self, player):
        if self.check_winner(player):
            self.handle_result(player)
        elif " " not in self.board:
            self.handle_result(None, "It's a tie!")

    def handle_result(self, player, message=None):
        self.playing = False
        if player:
            TicTacToe.result = f"{player} wins!"
            self.update_score(player)
            self.highlight_winner(player)
        else:
            TicTacToe.result = message
            self.ties += 1
            self.highlight_tie()

        self.update_score_label()
        self.disable_buttons()
        messagebox.showinfo("Game Over", TicTacToe.result)

    def highlight_winner(self, player):
        for indices in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
            if all(self.board[i] == player for i in indices):
                for j in indices:
                    self.buttons[j].config(bg="blue")

    def highlight_tie(self):
        for button in self.buttons:
            button.config(bg="red")

    def clear_colors(self):
        for button in self.buttons:
            button.config(bg="SystemButtonFace")

    def disable_buttons(self):
        for button in self.buttons:
            button.config(state=tk.DISABLED)

    def enable_buttons(self):
        for button in self.buttons:
            button.config(state=tk.NORMAL)

    def check_winner(self, player):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        return any(all(self.board[i] == player for i in indices) for indices in winning_combinations)

    def restart(self):
        self.board = [" " for _ in range(9)]
        for button in self.buttons:
            button.config(text=" ", state=tk.NORMAL, bg="SystemButtonFace")
        self.playing = True
        TicTacToe.result = None
        self.update_score_label()

    def update_score(self, player):
        if player == "X":
            self.user_wins += 1
        else:
            self.computer_wins += 1

    def update_score_label(self):
        self.score_label.config(text=f"You: {self.user_wins} Computer: {self.computer_wins} Ties: {self.ties}")

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
