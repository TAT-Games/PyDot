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


class Level1(Node):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Level1"
        player = Player.new()
        player.name = "Player 1"
        self.add_node(player)
        time: float = 0.0
       
        
    
class Level2(Node):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Level2"
        player = Player.new()
        player.name = "Player 2"
        self.add_node(player)
        print(self.get_child(0))
        self.set_process(False)
        self.set_physics_process(False)
        


world_instance = Level2.new().to_scene()


def main():
    Godot.set_main_scene(world_instance)
    Godot.run()
    

if __name__ == "__main__":
    main()