from gestures import Gestures

from player import Player

player = Player()

gestures = Gestures()


class Spock(Gestures):
    def __init__(self):
        self.win = bool
        super().__init__()

    def spock_win(self):
        self.win = player.gestures[0] or player.gestures[4]
