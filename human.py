from player import Player


class Human(Player):
    def __init__(self):
        self.name = ""
        super().__init__()

    def choose_gesture(self):
        self.gestures[0] = 0
        self.gestures[1] = 1
        self.gestures[2] = 2
        self.gestures[3] = 3
        self.gestures[4] = 4
        response = input(f"Pick a gesture: rock, spock, paper, lizard, or scissors.")
        if response == "rock":
            self.chosen_gesture = 0
        elif response == "spock":
            self.chosen_gesture = 1
        elif response == "paper":
            self.chosen_gesture = 2
        elif response == "lizard":
            self.chosen_gesture = 3
        elif response == "scissors":
            self.chosen_gesture = 4
        else:
            print("not valid selection, try again")
        if self.chosen_gesture == 0:
            print("Player picks rock.")
        elif self.chosen_gesture == 1:
            print("Player picks spock.")
        elif self.chosen_gesture == 2:
            print("Player picks paper.")
        elif self.chosen_gesture == 3:
            print("Player picks lizard.")
        elif self.chosen_gesture == 4:
            print("Player picks scissors.")
