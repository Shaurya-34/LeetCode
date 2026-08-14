# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = 0
        if root is None:
            return 0
        else:
            right = self.maxDepth(root.right)
            left = self.maxDepth(root.left)

            count = 1+ max(right, left)
        return count