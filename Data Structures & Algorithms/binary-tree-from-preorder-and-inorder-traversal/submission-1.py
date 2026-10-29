# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx_map = {val: i for i, val in enumerate(inorder)}

        def build(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None

            root_val = preorder[pre_left]
            root = TreeNode(root_val)

            idx = idx_map[root_val]

            left_size = idx - in_left

            root.left = build(
                pre_left + 1,
                pre_left + left_size,
                in_left,
                idx - 1
            )

            root.right = build(
                pre_left + left_size + 1,
                pre_right,
                idx + 1,
                in_right
            )

            return root

        n = len(preorder)
        return build(0, n - 1, 0, n - 1)