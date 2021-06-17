from gesture_class import GesturesClass



from player import Player

player = Player()

gestures_class = GesturesClass()


class Rock(GesturesClass):
    def __init__(self):
        self.win =bool
        super().__init__()

    def rock_win(self):
        self.gestures_class.rock.win == gestures_class.scissors or gestures_class.lizard
