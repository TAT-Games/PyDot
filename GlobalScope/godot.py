import sys; sys.path.append(".")
import pygame

from MyLib import  Vector2, singleton
from pygame.locals import *

from GlobalScope.scene import Scene
from GlobalScope.functions import Color, printErr
from GlobalScope.sceneTree import SceneTree
from GlobalScope.texture import Texture


@singleton
class Godot:
    """Create a single-window application with multiple scenes"""
    def __init__(self) -> None:
        self.__flags: int = 0
        self.__window_size: Vector2 = Vector2(500, 500)
        self.__window_title: str = "Godot Python Project (Debug)"
        self.__icon: Texture = Texture("icon.png")
        self.__background_colour: Color = Color("grey")
        self.__main_scene: Scene = None
    
    
    def init(self):
        """Initializes pygame and application"""
        pygame.init()
        self.__running = True
        
        self.set_window_size(self.__window_size, self.__flags)
        self.set_window_title(self.__window_title)
        self.set_window_icon(self.__icon)
        
    def set_window_size(self, size: Vector2, __flags: int = 0):
        """Sets window/screen size."""
        self.__window_size = size
        self.__flags = __flags
        self.__screen = pygame.display.set_mode((size.x, size.y), __flags)


    def set_window_title(self, title: str):
        """Sets the window's title/caption"""
        pygame.display.set_caption(title, "Arthur")


    def set_window_icon(self, icon: Texture):
        """Set's the window's icon"""
        self.__icon = icon
        pygame.display.set_icon(icon.get_data())


    def set_background_color(self, color: str):
        """Sets the background Color"""
        self.__background_colour = Color(color)
    
    
    def set_main_scene(self, scene: Scene):
        """Sets the main scene"""
        self.__main_scene = scene
    

    def get_window_size(self) -> Vector2:
        """Returns the window/screen size as a vector2 object"""
        return self.__window_size
    
    
    def run(self):
        """Run the main loop"""
        if self.__main_scene == None:
            printErr("No Main Scene Set", "GodotError" )
        
        else:
            SceneTree.change_current_scene(self.__main_scene)
            
        while self.__running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__running = False
                
                if event.type == KEYDOWN:
                    pass
            
            self.__screen.fill(self.__background_colour)
            
            SceneTree._process()

            pygame.display.flip()
            
        pygame.quit()


    # Disabled for now
    # def do_shortcut(self, event: pygame.Event):
    #     """Find the key/mod combination in the dictionary and execute cmd."""
    #     key = event.key
    #     modifier =  event.mod
    #     if (key, modifier) in self.shortcuts:
    #         exec(self.shortcuts[key, modifier])
    
    
    def toggle_fullscreen(self):
        """Toggle between full screen and widowed screen."""
        self.__flags = FULLSCREEN
        self.set_screen_size(Vector2.ZERO)
    
    
    def toggle_resizable(self):
        """Toggle between resizable and fixed-size window."""
        self.__flags = RESIZABLE
        pygame.display.set_mode(self.__window_size, self.__flags)
    
    
    def toggle_borderless(self):
        """Toggle between frame and no-frame window."""
        self.__flags = NOFRAME
        pygame.display.set_mode(self.__window_size, self.__flags)
