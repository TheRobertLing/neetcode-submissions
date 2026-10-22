# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter is either
        # length of right subtree
        # lenght of left subtree
        # sum of left and right subtree

        if root is None:
            return 0

        # Question
        # how do we get the length of the left and right subtree at every level
        # a bottom up approach would work better where length is calculated from the leave nodes

        # For each node, store the length of the left and right nodes
        # determine if its the longest path between any two nodes by using max()
        # return the max of the left and right path

        # Write a basic post order traversal

        diameter = 0

        def dfs(node):
            nonlocal diameter

            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            diameter = max(diameter, left, right, left + right)

            return max(1 + left, 1 + right)

        dfs(root)

        return diameter

        