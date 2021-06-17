from ai import Ai

from human import Human

from player import Player

from gesture_class import Gestures


player = Player()


class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = Ai()

    def run_game(self):
        self.welcome_message()
        self.game_rules()
        self.choose_game_mode()
        self.round()
        # self.complicated_round()
        self.declare_winner()
        # self.play_again()
        # Play Again? - not MVP

    def welcome_message(self):
        print("Welcome to Rock Paper Scissor Lizard Spock.")

    def game_rules(self):
        print("#Here are the rules#\nWINNER IS BEST OF 3!!!\nRock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock")

    def choose_game_mode(self):
        while True:
            response = input("\nHow many players? (1 or 2)")
            if int(response) == 1:
                self.player_two = Ai()
                break
            elif int(response) == 2:
                self.player_two = Human()
                break
            else:
                print("Try Again. How many players? (1 or 2)")

    def round(self):
        while self.player_one.score < 2 and self.player_two.score < 2:
            print("\nPlayer One's turn!")
            self.player_one.choose_gesture()
            print("\nPlayer Two's turn!")
            self.player_two.choose_gesture()
            result = (self.player_one.chosen_gesture - self.player_two.chosen_gesture) % 5
            if result == 0:
                print("Player One and Player Two tie round!")
            elif result >= 3:
                print("Player Two wins round")
                self.player_two.score += 1
            else:
                print("Player One wins round!")
                self.player_one.score += 1

    def gesture_class_round(self):
        print("\nPlayer One's turn!")
        self.player_one.choose_gesture_class()
        print("\nPlayer Two's turn!")
        self.player_two.choose_gesture_class()

    def declare_winner(self):
        if self.player_one.score == 2:
            print("\n###Player One has won RPSLS!!###\n")
        elif self.player_two.score == 2:
            print("\n###Player Two has won RPSlS!!###\n")

    def play_again(self):
        while True:
            replay_answer = input("Do you want to play again?(y/n)")
            if replay_answer == "y":
                self.run_game()
                break
            elif replay_answer == "n":
                print("Thank you for playing!")
                break
            else:
                print("That is not a valid response. Please try again.")
