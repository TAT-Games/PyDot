from pygame import Event

class InputEvent:
    def __init__(self, data: Event) -> None:
        self.handled: bool = False
        self.data = data