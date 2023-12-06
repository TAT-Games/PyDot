class Object:
    """A base class for all objects in the game"""
    def __init__(self) -> None:
        pass
    @classmethod
    def new(cls):
        return cls()