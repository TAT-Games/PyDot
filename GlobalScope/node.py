import sys; sys.path.append(".")
from GlobalScope.object import Object


class Node(Object):
    """A base class for all nodes"""
    def __init__(self) -> None:
        """Initializes the Node"""
        super().__init__()
        self.__children: dict = {}
        self.name = "Node"
        self.__parent: Node = None
        
    
    def _enter_tree(self):
        """Called when the node enters the scene for the first time"""
        print(f"{self.name} is entering tree")
        children: list = self.get_children()
        for child in children:
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
        pass
    
    
    def _process(self, delta: float):
        """Called every process frame"""
        print(f"{self.name}: Process")
        children = self.get_children()
        for node in children:
            if node in self.__children:
                node._process(delta)

    
    def _physics_process(self, delta: float):
        """Called every physics frame"""
        print(f"{self.name}: Physics Process")
        children = self.get_children()
        for node in children:
            if node in self.__children:
                node._physics_process(delta)
        
    
    def get_node(self, node_name: str):
        """Used to get a node from the __children"""
        children = self.get_children()
        if node_name in children:
            return self.__children[node_name]
        
        else:
            return None
    
    
    def get_parent(self):
        """Gets the node's parent"""
        return self.__parent


    def get_children(self):
        """Returns this node's children """
        children: list = []
        for node in self.__children.values():
            children.append(node)
        
        return children
    
    
    def add_node(self, node: 'Node'):
        """Adds to children"""
        if node.name in self.__children and node != self.__children[node.name]:
            node.name += str(len(self.__children) - 1)
            
        self.__children[node.name] = node
        node.__parent = self
        node._enter_tree()
    
    
    def remove_node(self, node: 'Node'):
        """Remove node from children"""
        self.__children.pop(node.name)
        node.__parent = None
        node._exit_tree()
    
    
    def queue_free(self):
        self.__parent = None
        children = self.get_children()
        for node in children:
            node.queue_free()
