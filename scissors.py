from gesture_class import GesturesClass

from player import Player

player = Player()

gestures_class = GesturesClass()


class Scissors(GesturesClass):
    def __init__(self):
        self.win = bool
        super().__init__()

    def scissors_win(self):
        gestures_class.scissors.win == gestures_class.paper or gestures_class.lizard