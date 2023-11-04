import sys; sys.path.append(".")
from pygame import Event, KEYDOWN, KEYUP
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
    
    
    def is_key_pressed(self, key: int) -> bool:
        """Checks if the key is pressed"""
        if self.__current_event == None:
            return False
        
        if self.__current_event.type == KEYDOWN:
            if self.__current_event.key == key:
                return True
        
        return False
    
    
    def is_key_released(self, key: int) -> bool:
        """Checks if the key is released"""
        if self.__current_event == None:
            return True
        
        if self.__current_event.type == KEYDOWN:
            if self.__current_event.key == key:
                return False
        
        return True