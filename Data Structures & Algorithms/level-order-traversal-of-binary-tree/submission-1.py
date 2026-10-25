# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        res = []
        q = deque([[root]])

        while q:
            level = q.popleft()

            curr_level = []
            next_level = []
            for node in level:

                curr_level.append(node.val)

                if node.left:
                    next_level.append(node.left)
                
                if node.right:
                    next_level.append(node.right)
            
            res.append(curr_level)

            if next_level:
                q.append(next_level)

        return res
