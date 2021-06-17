from player import Player

from gesture_class import GesturesClass

gesture_class = GesturesClass()


import random


class Ai(Player):
    def __init__(self):
        self.name = "Computer"
        self.score = 0
        super().__init__()

    def choose_gesture(self):
        self.gestures[0] = 0
        self.gestures[1] = 1
        self.gestures[2] = 2
        self.gestures[3] = 3
        self.gestures[4] = 4
        self.chosen_gesture = random.randint(0, 4)
        if self.chosen_gesture == 0:
            print("Computer picks rock.")
        elif self.chosen_gesture == 1:
            print("Computer picks spock.")
        elif self.chosen_gesture == 2:
            print("Computer picks paper.")
        elif self.chosen_gesture == 3:
            print("Computer picks lizard.")
        elif self.chosen_gesture == 4:
            print("Computer picks scissors.")

    def choose_gesture_class(self):
        gesture_class.rock = 0
        gesture_class.spock = 1
        gesture_class.paper = 2
        gesture_class.lizard = 3
        gesture_class.scissors = 4
        self.chosen_gesture = random.randint(0, 4)
        if self.chosen_gesture == 0:
            print("Computer picks rock.")
        elif self.chosen_gesture == 1:
            print("Computer picks spock.")
        elif self.chosen_gesture == 2:
            print("Computer picks paper.")
        elif self.chosen_gesture == 3:
            print("Computer picks lizard.")
        elif self.chosen_gesture == 4:
            print("Computer picks scissors.")
