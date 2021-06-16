from gestures import Gestures

from player import Player

player = Player()

gestures = Gestures()


class Lizard(Gestures):
    def __init__(self):
        self.win = bool
        super().__init__()

    def lizard_win(self):
        self.win = player.gestures[1] or player.gestures[2]