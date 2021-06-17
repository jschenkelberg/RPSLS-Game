from gesture_class import GesturesClass

from player import Player

player = Player()

gestures = GesturesClass()


class Scissors(GesturesClass):
    def __init__(self):
        self.win = bool
        super().__init__()

    def scissors_win(self):
        gestures.scissors.win == gestures.paper or gestures.lizard