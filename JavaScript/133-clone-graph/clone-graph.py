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
        if not node:
            return None
        cloned_node = Node(node.val)
        visited = {}


        def dfs(cloned_node, original_node):
            visited[original_node] = cloned_node

            if original_node.neighbors:
                for nei in original_node.neighbors:
                    if nei in visited and cloned_node not in visited[nei].neighbors:
                        visited[nei].neighbors.append(cloned_node)
                    if nei not in visited:
                        new_node = Node(nei.val)
                        cloned_node.neighbors.append(new_node)
                        new_node.neighbors.append(cloned_node)
                        dfs(new_node, nei)

        dfs(cloned_node, node)

        return cloned_node