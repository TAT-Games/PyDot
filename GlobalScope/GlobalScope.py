import sys, pygame
sys.path.append(".")
from pygame.locals import *
from pygame import Color
from MyLib import *

# enums

# 

# OBJECTS
class Object:
    def __init__(self) -> None:
        pass

    @classmethod
    def new(cls):
        return cls()


class Texture(Object):
    def __init__(self, filepath: str):
        """A base class for textures used in the game"""
        self.data =  pygame.image.load(filepath)
        
      
   
    def get_data(self) -> pygame.Surface:
        """Returns the image data as a pygame surface"""
        return self.data


class Node(Object):
    def __init__(self) -> None:
        """Initializes the Node"""
        super().__init__()
        self.children: dict = {}
        self.name = "Node"
        self.__parent: Node = None
        
    
    def _enter_tree(self):
        """Called when the node enters the scene for the first time"""
        print(f"{self.name} is entering tree")
        for child in self.children:
            child._enter_tree()
        
        for child in self.children:
            child._ready()
        
        self._ready()
    
    
    def _exit_tree(self):
        """Called when the node is about to leave the scene"""
        print(f"{self.name} is exiting tree")
        for child in self.children:
            child._exiting_tree()
        
        self._exit_tree()
    
    
    def _ready(self):
        """Called when the node is ready"""
        print(f"{self.name} is ready")
        pass
    
    
    def _process(self, delta: float):
        """Called every process frame"""
        print(f"{self.name}: Process")
    
        for node in self.children.values():
            node._process(delta)

    
    def _physics_process(self, delta: float):
        """Called every physics frame"""
        print(f"{self.name}: Physics Process")
        for node in self.children.values():
            node._physics_process(delta)
        
    
    def get_node(self, node_name: str):
        """Used to get a node from the children"""
        if node_name in self.children:
            return self.children[node_name]
        
        else:
            return None


    def add_node(self, node: 'Node'):
        """Adds a node to this Node's Children"""
        if node.name in self.children and node != self.children[node.name]:
            node.name += str(len(self.children) - 1)
            
        self.children[node.name] = node
        node.__parent = self
    
    
    def queue_free(self):
        del self
    
    
    def get_parent(self):
        """Gets the node's parent"""
        return self.__parent


class Scene(Node):
    "A scene"
    def __init__(self) -> None:
        """Initializes the Scene"""
        super().__init__()
        



# SINGLETONS
@singleton
class SceneTree:
    """Manages the current scene"""
    def __init__(self) -> None:
        self.current_scene: Scene  = None
        

    def get_current_scene(self):
        """Gets the current scene"""
        return self.current_scene

    
    def change_current_scene(self, scene: 'Scene'):
        """Changes the current scene"""
        self.current_scene = scene
        

    def _process(self):
        if self.current_scene  != None:
            self.current_scene._process(1.0)
            self.current_scene._physics_process(1.0)
            
        else:
            printErr("No Current scene set.", "SceneTree")
        
        
@singleton
class Godot:
    """Create a single-window application with multiple scenes"""
    def __init__(self) -> None:
        self.__flags: int = 0
        self.__window_size: Vector2 = Vector2(500, 500)
        self.__window_title: str = "Godot Python Project (Debug)"
        self.__icon: Texture = Texture("GlobalScope/icon.png")
        self.__background_colour: Color = Color("grey")
    
    
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


    def get_window_size(self) -> Vector2:
        """Returns the window/screen size as a vector2 object"""
        return self.__window_size
    
    
    def set_background_color(self, color: str):
        self.__background_colour = Color(color)
    

    def run(self):
        """Run the main loop"""
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


def printErr(text: str, ErrorType: str = "ERROR"):
    __dashes: str = "-" * ((len(text) // 2) - (len(ErrorType) // 2))
    print(f"\n{__dashes}ERROR{__dashes}\n{text}")
    quit()
    

def main():
    texture = Texture("icon.png")
    print(Color("Blue"))
    print(Vector2(0,0))
    print(Vector2(-1, 0))

if __name__ == "__main__":
    main()