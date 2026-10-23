# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # traverse both

        is_same = True

        def dfs(node_p, node_q):
            nonlocal is_same

            # Both are None
            if node_p is None and node_q is None:
                return

            # Either one is None
            if node_p is None and node_q is not None:
                is_same = False
                return

            if node_q is None and node_p is not None:
                is_same = False
                return

            if node_p.val != node_q.val:
                is_same = False
                return

            dfs(node_p.left, node_q.left)
            dfs(node_p.right, node_q.right)

        
        dfs(p, q)

        return is_same