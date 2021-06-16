from ai import Ai

from human import Human

from player import Player

player = Player()

class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = None


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
        print("#Here are the rules#\nRock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock")

    def choose_game_mode(self):
        print("\nHow many players?")
        response = input()
        if int(response) == 1:
            self.player_two = Ai()
        elif int(response) == 2:
            self.player_two = Human()





    def round(self):

        print("Player One's turn!\n")
        self.player_one.choose_gesture()
        print("\nPlayer Two's turn!")
        self.player_two.choose_gesture()
        result = (self.player_one.chosen_gesture - self.player_two.chosen_gesture) %5
        if result == 0:
            print("Player One and Player Two tie!")
        elif result >= 3:
            print("Player Two wins")
            
        else:
            print("Player One wins!")

