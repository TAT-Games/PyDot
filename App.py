import sys; sys.path.append(".")
from __init__ import *

Godot.init()

Godot.set_window_size(Vector2(500, 400))
Godot.set_background_color("grey")


class Player(Node):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Player"


    def attack(self, damage: int) -> None:
        print(f"Attack: {damage}")
    
    
    def _process(self, delta: float):
        if Input.is_key_pressed(K_UP):
            print("Up Arrow pressed")
        
        if Input.is_mouse_button_pressed(BUTTON_LEFT):
            print("Mouse button pressed")
        
        
class Level1(Node):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Level1"
        player = Player.new()
        player.name = "Player 1"
        self.add_child(player)
        time: float = 0.0
       
        
class Level2(Node):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Level2"
        player = Player.new()
        player.name = "Player 2"
        self.add_child(player)
        self.set_process(False)
        self.set_physics_process(False)
        

world_instance = Level2()


def main():
    Godot.set_main_scene(world_instance)
    Godot.run()
    

if __name__ == "__main__":
    main()