
from player import Player

player = Player()


class GesturesClass:
    def __init__(self):
        self.rock = 0
        self.spock = 1
        self.paper = 2
        self.lizard = 3
        self.scissors = 4
        self.compare = int


    def gesture_victories(self):
        victories = {
            self.rock: [self.scissors, self.lizard],
            self.spock: [self.scissors, self.rock],
            self.paper: [self.spock, self.rock],
            self.lizard: [self.spock, self.paper],
            self.scissors: [self.paper, self.lizard]
        }

    def compare_for_win(self):
        pass


