from player import Player


class Human(Player):
    def __init__(self):
        self.name = ""
        self.score = 0
        super().__init__()

    def choose_gesture(self):
        while True:
            self.gestures[0] = 0
            self.gestures[1] = 1
            self.gestures[2] = 2
            self.gestures[3] = 3
            self.gestures[4] = 4
            response = input(f"Pick a gesture: rock, paper, scissors, lizard, or spock.")
            if response == "rock":
                self.chosen_gesture = 0
                break
            elif response == "spock":
                self.chosen_gesture = 1
                break
            elif response == "paper":
                self.chosen_gesture = 2
                break
            elif response == "lizard":
                self.chosen_gesture = 3
                break
            elif response == "scissors":
                self.chosen_gesture = 4
                break
            # if self.chosen_gesture == 0:
            #     print("Player picks rock.")
            # elif self.chosen_gesture == 1:
            #     print("Player picks spock.")
            # elif self.chosen_gesture == 2:
            #     print("Player picks paper.")
            # elif self.chosen_gesture == 3:
            #     print("Player picks lizard.")
            # elif self.chosen_gesture == 4:
            #     print("Player picks scissors.")
            else:
                print("not valid selection, try again")
