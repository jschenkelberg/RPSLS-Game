from gesture_class import GesturesClass

from player import Player


player = Player()

gestures_class = GesturesClass()


class Spock(GesturesClass):
    def __init__(self):
        self.compare = gestures_class.scissors or gestures_class.rock
        super().__init__()

    def spock_win(self):
        self.spock.win == gestures_class.scissors or gestures_class.rock
