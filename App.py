import GlobalScope
from MyLib import *
from GlobalScope import *

Godot.init()

Godot.set_window_size(Vector2(500, 400))
Godot.set_background_color("grey")



class Player(Node):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Player"


    def attack(self, damage: int) -> None:
        print(f"Attack: {damage}")


class World(Node):
    def __init__(self) -> None:
        super().__init__()
        player = Player.new()
        self.add_node(player)
        
world_instance = World.new()
Scene(world_instance)

def main():
    Godot.set_main_scene(world_instance)
    Godot.run()
    

if __name__ == "__main__":
    main()