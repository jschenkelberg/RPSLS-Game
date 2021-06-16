from gestures import Gestures


from player import Player

player = Player()

gestures = Gestures()


class Rock(Gestures):
    def __init__(self):
        self.win =bool
        super().__init__()

    def rock_win(self):
        self.win = player.gestures[3] or player.gestures[4]
