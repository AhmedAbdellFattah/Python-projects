import random

class GuessingGame:
    def __init__(self):
        self.attempts_list = []
        self.attempts = 0
        self.rand_number = random.randint(1, 10)
        self.player_name = ""

    def show_score(self):
        """Displays the current high score or prompts the player to start playing."""
        if not self.attempts_list:
            print("There's currently no high score, start playing!")
        else:
            print(f"The current high score is {min(self.attempts_list)} attempts")

    def play_game(self):
        """Starts the guessing game."""
        print("Hello player! Welcome to the guessing game!")
        self.player_name = input("What's your name? ")
        wanna_play = input(f"Hi, {self.player_name}, would you like to play the guessing game? (Enter Yes/No): ").lower()

        if wanna_play == "no":
            print("That's cool, thanks!")
            exit()
        else:
            self.show_score()

        while wanna_play == "yes":
            self.take_guess()

    def take_guess(self):
        """Handles the player's input for guessing the number."""
        try:
            guess = int(input("Pick a number between 1 and 10: "))
            self.validate_guess(guess)

            self.attempts += 1

            if guess == self.rand_number:
                self.handle_correct_guess()
            elif guess > self.rand_number:
                print("It's lower!")
            else:
                print("It's higher!")

        except ValueError as err:
            print(err)

    def validate_guess(self, guess):
        """Validates if the guess is within the given range."""
        if not 1 <= guess <= 10:
            raise ValueError("Please guess a number within the given range")

    def handle_correct_guess(self):
        """Handles the scenario when the player guesses the correct number."""
        print("Nice, you got it!")
        print(f"It took you {self.attempts} attempts!")
        self.update_high_score()

        wanna_play = input("Would you like to play again (Enter Yes/No): ").lower()

        if wanna_play == "no":
            print("That's cool, have a good day.")
            exit()
        else:
            self.reset_game()

    def update_high_score(self):
        """Updates the high score list with the current number of attempts."""
        self.attempts_list.append(self.attempts)

    def reset_game(self):
        """Resets the game for a new round."""
        self.attempts = 0
        self.rand_number = random.randint(1, 10)
        self.show_score()

# Instantiate the GuessingGame class and start playing
game = GuessingGame()
game.play_game()
