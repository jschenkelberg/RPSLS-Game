from gesture_class import GesturesClass

from player import Player



player = Player()

gestures_class = GesturesClass()


class Lizard(GesturesClass):
    def __init__(self):
        self.win = bool
        super().__init__()

    def lizard_win(self):
        gestures_class.lizard.win == gestures_class.spock or gestures_class.paper
