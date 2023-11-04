import sys; sys.path.append(".")

from GlobalScope.functions import printErr
from GlobalScope.object import Object


class Node(Object):
    """A base class for all nodes"""
    def __init__(self) -> None:
        """Initializes the Node"""
        super().__init__()
        self.__children: dict = {}
        self.__parent: Node = None
        self.__is_scene: bool = False
        self.__can_process: bool = True
        self.__can_physics_process: bool = True
        self.owner: Node = None
        self.name = "Node"
        
    
    def _enter_tree(self):
        """Called when the node enters the scene for the first time"""
        print(f"{self.name} is entering tree")
        children: list = self.get_children()
        for child in children:
            child.owner = self.owner
            child._enter_tree()
        
        for child in children:
            child._ready()
        
        self._ready()
    
    
    def _exit_tree(self):
        """Called when the node is about to leave the scene"""
        print(f"{self.name} is exiting tree")
        children = self.get_children()
        for child in children:
            child._exit_tree()
    
    
    def _ready(self):
        """Called when the node is ready"""
        print(f"{self.name} is ready")
    
    
    def _process(self, delta: float):
        """Called every process frame"""
        if not self.__can_process:
            return
        
        print(f"{self.name}: Process")
        children = self.get_children()
        for node in children:
            node._process(delta)

    
    def _physics_process(self, delta: float):
        """Called every physics frame"""
        if not self.__can_physics_process:
            return
        
        print(f"{self.name}: Physics Process, {delta}")
        children = self.get_children()
        for node in children:
            node._physics_process(delta)
       
        
    def set_process(self, value: bool) -> None:
        """Enables or disables this node's process call with boolean value"""
        self.__can_process = value
     
        
    def set_physics_process(self, value: bool) -> None:
        """Enables or disables this node's physics process call with boolean value"""
        self.__can_physics_process = value
        

    def add_node(self, node: 'Node'):
        """Adds to children"""
        if node.name in self.__children and node != self.__children[node.name]:
            node.name += str(len(self.__children) - 1)
            
        self.__children[node.name] = node
        node.__parent = self
        if self.owner != None:
            node.owner = self.owner
            node._enter_tree()
    
    
    def remove_node(self, node: 'Node') -> None:
        """Remove node from children"""
        self.__children.pop(node.name)
        node.__parent = None
        if self.owner != None:
            node.owner = None
            node._exit_tree()
    
    
    def get_node(self, node_name: str) -> 'Node':
        """Used to get a node from the __children"""
        children = self.get_children()
        if node_name in children:
            return self.__children[node_name]
        
        else:
            return None


    def get_children(self) -> list:
        """Returns this node's children """
        children: list = []
        for node in self.__children.values():
            children.append(node)
        
        return children
    
    
    def get_child(self, index: int):
        """Returns a child from the specified index"""
        children = self.get_children()
        if index + 1 > len(children):
            printErr("Child Index is out of range", "IndexError", "Try a lower number when getting child")
        
        return children[index]
    
    
    def get_parent(self) -> 'Node':
        """Gets the node's parent"""
        return self.__parent
    
    
    def to_scene(self) -> 'Node':
        """Transforms a node to a scene"""
        self.owner = self
        self.__is_scene = True
        return self
        
        
    def is_scene(self) -> bool:
        """Returns a bool telling whether node is a scene"""
        if self.owner == None:
            return False
        
        else:
            return self.__is_scene and self.owner == self
    

    def queue_free(self):
        """Clears all possible refs to node"""
        self.__parent = None
        children = self.get_children()
        for node in children:
            self.remove_node(node)