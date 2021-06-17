from gesture_class import GesturesClass


from player import Player

player = Player()

gestures_class = GesturesClass()


class Rock(Gestures):
    def __init__(self):
        self.win =bool
        super().__init__()

    def rock_win(self):
        gestures_class.rock.win == gestures_class.scissors or gestures_class.lizard
