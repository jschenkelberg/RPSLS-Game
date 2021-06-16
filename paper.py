from gestures import Gestures

from player import Player

player = Player()

gestures = Gestures()


class Paper(Gestures):
    def __init__(self):
        self.win = bool
        super().__init__()

    def paper_win(self):
        self.win = player.gestures[0] or player.gestures[1]
