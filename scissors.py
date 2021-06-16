from gestures import Gestures

from player import Player

player = Player()

gestures = Gestures()


class Scissors(Gestures):
    def __init__(self):
        self.win = bool
        super().__init__()

    def scissors_win(self):
        self.win = player.gestures[2] or player.gestures[3]