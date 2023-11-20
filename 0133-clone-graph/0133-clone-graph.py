"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mapping = {}

        def helper(node):
            
            if node is None:
                return None
            
            copy = Node(node.val)
            mapping[node.val] = copy

            for neighbor in node.neighbors:
                if neighbor.val not in mapping:
                    copy.neighbors.append(helper(neighbor))
                else:
                    copy.neighbors.append(mapping[neighbor.val])

            return copy

        return helper(node)