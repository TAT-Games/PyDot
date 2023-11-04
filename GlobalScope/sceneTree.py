import sys; sys.path.append(".")

from GlobalScope.node import Node
from GlobalScope.functions import printErr
from MyLib import singleton


@singleton
class SceneTree:
    """Manages the current scene"""
    def __init__(self) -> None:
        self.__current_scene: 'Node' = None
        

    def get_current_scene(self):
        """Gets the current scene"""
        return self.__current_scene

    
    def change_current_scene(self, scene: 'Node'):
        """Changes the current scene"""
        if scene.owner == scene and scene.__is_scene:
            self.__current_scene._exit_tree()
            self.__current_scene = scene
            self.__current_scene._enter_tree()
        
        else:
            printErr("Invalid Scene", "SceneTree Error", "Use the Scene() function to transform a node to a scene")


    def _process(self, delta: float):
        if self.__current_scene  != None:
            self.__current_scene._process(delta)
            self.__current_scene._physics_process(delta)
            
        else:
            printErr("No Current scene set.", "SceneTree")