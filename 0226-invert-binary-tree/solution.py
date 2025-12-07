# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Edge case if the root is empty return None
        # Create a dfs function
        # Store both left and right children
        # Assign the left to the recursively called right child
        # Assign the right to the recursively called left child
        # Return root
        def dfs(root):
            if root is None:
                return root

            right = root.right
            root.right = dfs(root.left)
            root.left = dfs(right)

            return root

        return dfs(root)

            
