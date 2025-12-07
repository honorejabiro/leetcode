# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Get the max of the left side and max of the right side
        # Return the sum of the too
        # If root is None return 0
        # Go to the left 
        # Go to the right
        # Add the path
        # Update the max path
        # Return max path
        result = 0
        def dfs(root):
            nonlocal result
            if root is None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            result = max(result, (left+right))
            return (max(left, right) + 1)

        dfs(root)
        return result
