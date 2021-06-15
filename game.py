from ai import Ai

from human import Human

from player import Player

class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = Human() or Ai()


    def run_game(self):
        self.welcome_message()
        self.game_rules()
    # 1 or 2 person game?
        self.choose_game_mode()
        # Round 1
        self.round()
    # Player 1 picks gesture
    # Player 2 or AI picks gesture
    # Winner score increases

        # Round 2
    # Player 1 picks gesture
    # Player 2 or AI picks gesture
    # Winner score increases (check for winner)

        #Round 3
    # Player 1 picks gesture
    # Player 2 or AI picks gesture
    # Winner score increases

    # Declare winner

    # Play Again? - not MVP
    pass

    def welcome_message(self):
        print("Welcome to Rock Paper Scissor Lizard Spock.")

    def game_rules(self):
        print("Here's how it works...")

    def choose_game_mode(self):
        print("How many players?")
        response = input()
        if response == 1:
            self.player_two = Ai()
        if response == 2:
            self.player_two = Human()




    def round(self):
        self.player_one.choose_gesture()
        self.player_two.choose_gesture()
        result = (self.player_one.chosen_gesture - self.player_two.chosen_gesture) %5
        if result == 0:
            print("Player One and Player two tie!")
        elif result >= 3:
            print("Player One wins!")
        else:
            print("Player Two wins!")