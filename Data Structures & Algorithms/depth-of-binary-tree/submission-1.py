# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        longest_path = 1

        def dfs(path_length, node):
            nonlocal longest_path

            if node is None:
                return

            if node.left is None and node.right is None:
                longest_path = max(longest_path, path_length)
                return

            dfs(path_length + 1, node.left)
            dfs(path_length + 1, node.right)

        dfs(1, root)
        return longest_path

        