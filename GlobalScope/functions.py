from pygame import Color

def printErr(error: str, ErrorType: str = "ERROR", help: str = ""):
    """Print an error to the terminal"""
    print(f"\n{ErrorType}: {error}")
    if help != "":
        print(f"> Help: {help}")
        
    quit()

