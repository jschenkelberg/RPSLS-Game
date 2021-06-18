from gesture_class import GesturesClass



from player import Player

player = Player()

gestures_class = GesturesClass()


class Rock(GesturesClass):
    def __init__(self):
        self.win =bool
        self.compare = gestures_class.scissors or gestures_class.lizard
        super().__init__()

    def rock_win(self):
        gestures_class.scissors or gestures_class.lizard
