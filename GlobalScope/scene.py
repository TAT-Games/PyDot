import sys; sys.path.append(".")
from GlobalScope.node import Node

def Scene(node: Node):
    node.owner = node
    node.__is_scene = True
    return node