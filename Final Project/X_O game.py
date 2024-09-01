import tkinter as tk
import random
from tkinter import messagebox

class TicTacToe:
    result = None  # Global variable to store the game result

    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")

        # Game variables
        self.board = [" " for _ in range(9)]
        self.playing = True
        self.user_wins = 0
        self.computer_wins = 0
        self.ties = 0

        # GUI elements
        self.score_label = tk.Label(master, text="You: 0 Computer: 0 Ties: 0", font=('Arial', 14))
        self.score_label.grid(row=0, column=0, columnspan=3)

        self.buttons = [tk.Button(master, text=" ", font=('Arial', 20), width=5, height=2, command=lambda j=j: self.click(j)) for j in range(9)]
        for i in range(3):
            for j in range(3):
                self.buttons[i*3 + j].grid(row=i+1, column=j)

        self.restart_button = tk.Button(master, text="Restart", font=('Arial', 14), command=self.restart)
        self.restart_button.grid(row=4, column=1)

        # Initialize the game
        self.restart()

    def click(self, i):
        if self.playing and self.board[i] == " ":
            self.board[i] = "X"
            self.buttons[i].config(text="X")
            self.check_and_handle_result("X")

            if self.playing:
                self.computer_turn()

    def computer_turn(self):
        winning_move = self.find_winning_move("O")
        blocking_move = self.find_winning_move("X")

        if winning_move is not None:
            self.board[winning_move] = "O"
            self.buttons[winning_move].config(text="O")
            self.check_and_handle_result("O")
        elif blocking_move is not None:
            self.board[blocking_move] = "O"
            self.buttons[blocking_move].config(text="O")
        else:
            choices = [i for i in range(9) if self.board[i] == " "]
            if choices:
                computer_choice = random.choice(choices)
                self.board[computer_choice] = "O"
                self.buttons[computer_choice].config(text="O")
                self.check_and_handle_result("O")

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
            self.playing = False
            TicTacToe.result = f"{player} wins!"
            if player == "X":
                self.user_wins += 1
            else:
                self.computer_wins += 1
            self.update_score_label()
            self.highlight_winner(player)
            self.disable_buttons()
            messagebox.showinfo("Game Over", TicTacToe.result)
        elif " " not in self.board:
            # Check if the board is full and it's a tie
            self.playing = False
            TicTacToe.result = "It's a tie!"
            self.ties += 1
            self.update_score_label()
            self.highlight_tie()
            self.disable_buttons()
            messagebox.showinfo("Game Over", TicTacToe.result)

    def highlight_winner(self, player):
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i + 1] == self.board[i + 2] == player:
                for j in range(i, i + 3):
                    self.buttons[j].config(bg="blue")

        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] == player:
                for j in range(i, i + 7, 3):
                    self.buttons[j].config(bg="blue")

        if self.board[0] == self.board[4] == self.board[8] == player:
            for j in range(0, 9, 4):
                self.buttons[j].config(bg="blue")

        if self.board[2] == self.board[4] == self.board[6] == player:
            for j in range(2, 7, 2):
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
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i + 1] == self.board[i + 2] == player:
                return True

        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] == player:
                return True

        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] == player:
            return True
        if self.board[2] == self.board[4] == self.board[6] == player:
            return True

        return False

    def restart(self):
        self.board = [" " for _ in range(9)]
        for button in self.buttons:
            button.config(text=" ", state=tk.NORMAL, bg="SystemButtonFace")  # Reset text, enable buttons, and remove colors
        self.playing = True
        TicTacToe.result = None  # Reset game result
        self.update_score_label()

    def update_score_label(self):
        self.score_label.config(text=f"You: {self.user_wins} Computer: {self.computer_wins} Ties: {self.ties}")

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()