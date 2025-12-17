# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # if number is less than or equal to the low we skip the left 
        # If number is greater than or equal to the high we skip the right
        # Else we traverse both
        res = 0
        
        def dfs(root):
            nonlocal res
            if root is None:
                return
            # Conditions
            if low < root.val < high:
                res += root.val
                dfs(root.left)
                dfs(root.right)
                
            elif root.val <= low:
                if root.val == low:
                    res += root.val
                dfs(root.right)
                
            elif root.val >= high:
                if root.val == high:
                    res += root.val
                dfs(root.left)
                
        dfs(root)
        return res
                
                
