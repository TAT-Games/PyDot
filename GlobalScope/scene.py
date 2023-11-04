import sys; sys.path.append(".")
from GlobalScope.node import Node

def Scene(node: Node):
    node.owner = node
    return node

