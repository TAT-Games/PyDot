import sys; sys.path.append(".")

from GlobalScope.node import Node
from GlobalScope.functions import printErr
from MyLib import singleton


@singleton
class SceneTree:
    """Manages the current scene"""
    def __init__(self) -> None:
        self.current_scene: Node  = None
        

    def get_current_scene(self):
        """Gets the current scene"""
        return self.current_scene

    
    def change_current_scene(self, scene: Node):
        """Changes the current scene"""
        self.current_scene = scene
        

    def _process(self):
        if self.current_scene  != None:
            self.current_scene._process(1.0)
            self.current_scene._physics_process(1.0)
            
        else:
            printErr("No Current scene set.", "SceneTree")