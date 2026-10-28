# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # for the left subtree
        # current bound: (X, Y)
        # left subtree bound: (X, Z)
        # right subtree bound: (Z, Y)

        def dfs(node, lower, upper):
            if node is None:
                return True

            return lower < node.val < upper and dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)

        return dfs(root, -math.inf, math.inf)


















