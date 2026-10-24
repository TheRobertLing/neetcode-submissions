# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        is_subtree = False

        def check_subtree(a, b):
            if a is None and b is None:
                return True

            if a is None and b is not None:
                return False
            if b is None and a is not None:
                return False
            
            if a.val == b.val:
                return check_subtree(a.left, b.left) and check_subtree(a.right, b.right)
            else:
                return False
            

        def dfs(node):
            nonlocal is_subtree

            if node is None:
                return
            
            is_subtree |= check_subtree(node, subRoot)
            
            dfs(node.left)
            dfs(node.right)


        dfs(root)

        return is_subtree
        
        