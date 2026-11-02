# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import json

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            if node is None:
                res.append(None)
                return

            res.append(node.val)

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return json.dumps(res)


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tree = iter(json.loads(data))

        def dfs():
            val = next(tree)

            if val is None:
                return None

            node = TreeNode(val)

            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()

            

