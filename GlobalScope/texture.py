from object import Object
from pygame import image
from pygame import Surface

class Texture(Object):
    """A base class for textures used in the game"""
    def __init__(self, filepath: str):
        self.__data = image.load(filepath)
        
   
    def get_data(self) -> Surface:
        """Returns the image data as a pygame surface"""
        return self.__data