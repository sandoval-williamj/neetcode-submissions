# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d = 0
        def helper(node: Optional[TreeNode]):
            if not node:
                return 0

            left = helper(node.left)
            right = helper(node.right)

            self.d = max(self.d, right + left)
        
            return 1 + max(right, left)
        helper(root)
    
        return self.d