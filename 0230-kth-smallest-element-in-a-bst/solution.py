# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Iterative 
        # Create a stack
        # While stack or root
        # Go to the furthest left
        # If root is None pop from the stack and add to the result
        # Update the pointer to right
        stack = []
        pointer = root
        res = []

        while stack or pointer:
            while pointer:
                stack.append(pointer)
                pointer = pointer.left

            node = stack.pop()
            res.append(node.val)
            pointer = node.right
        
        return res[k-1]
