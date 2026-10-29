# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in order traversal

        idx = 1
        value = 0


        def dfs(node):
            nonlocal value
            nonlocal idx

            if node is None:
                return
            
            dfs(node.left)

            if idx == k:
                value = node.val
            
            idx += 1


            dfs(node.right)

        dfs(root)

        return value