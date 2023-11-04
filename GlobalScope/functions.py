from pygame import Color
from GlobalScope.sceneTree import SceneTree as __st

def printErr(error: str, ErrorType: str = "ERROR", help: str = ""):
    """Print an error to the terminal"""
    print(f"\n{ErrorType}: {error}")
    if help != "":
        print(f"> Help: {help}")
        
    quit()

def get_tree() -> __st:
    return __st