# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True
        if not q or not p:
            return False
        
        t_p = []
        t_q = []
        t_p.append(p)
        t_q.append(q)

        while t_p and t_q:
            c_q = t_q.pop()
            c_p = t_p.pop()
            is_right, is_left = False, False

            if c_q.val != c_p.val:
                return False
            
            if c_q.right:
                t_q.append(c_q.right)
                is_right = True
            if c_p.right:
                t_p.append(c_p.right)
            elif is_right:
                return False

            if c_q.left:
                t_q.append(c_q.left)
                is_left = True
            if c_p.left:
                t_p.append(c_p.left)
            elif is_left:
                return False

        if t_p or t_q:
            return False

        return True