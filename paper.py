from gesture_class import GesturesClass

from player import Player



player = Player()

gestures_class = GesturesClass()


class Paper(GesturesClass):
    def __init__(self):
        self.win = bool
        self.compare = gestures_class.spock or gestures_class.rock
        super().__init__()

    def paper_win(self):
        gestures_class.spock or gestures_class.rock
