from GlobalScope import *

Godot.init()

Godot.set_window_size(Vector2(500, 400))
Godot.set_background_color("grey")


class Player(Node):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Player"


    def attack(self, damage: int):
        print(f"Attack: {damage}")

 
main_scene = Scene()
some_node = Node.new()
some_node.name = "Arthur"
main_scene.add_node(some_node)
main_scene.add_node(Node())
main_scene.add_node(Node.new())


SceneTree.change_current_scene(main_scene)



def main():
    Godot.run()
    


if __name__ == "__main__":
    main()

