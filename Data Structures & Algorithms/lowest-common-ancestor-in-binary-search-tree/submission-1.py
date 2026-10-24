# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Binary search tree so can use the property of binary tree to do a binary search

        # if one value is on the one side and one value is on the other side, then the current node is the ancestor
        # otherwise go down a branch

        lca = root

        while True:

            # Binary search
            if lca.val == p.val or lca.val == q.val:
                return lca

            if p.val < lca.val < q.val or q.val < lca.val < p.val:
                return lca

            if lca.val < p.val and lca.val < q.val:
                lca = lca.right
            
            if lca.val > p.val and lca.val > q.val:
                lca = lca.left



















