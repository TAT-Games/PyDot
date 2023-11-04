import sys; sys.path.append(".")
from pygame import Event
from GlobalScope.singleton import singleton

@singleton
class Input:
    """Helper singleton to get input"""
    def __init__(self) -> None:
        self.__current_event: Event = None
    
    
    def _update_event(self, event: Event) -> None:
        """Updates the current event"""
        self.__current_event = event
        print(event)
    
    
    
    