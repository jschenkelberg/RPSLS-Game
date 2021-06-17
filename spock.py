from gesture_class import GesturesClass

from player import Player

player = Player()

gestures_class = GesturesClass()


class Spock(Gestures):
    def __init__(self):
        self.win = bool
        super().__init__()

    def spock_win(self):
        gestures_class.spock.win == gestures_class.scissors or gestures_class.rock
