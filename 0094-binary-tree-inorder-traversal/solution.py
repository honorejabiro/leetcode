# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        stack = []
        res = []
        p = root

        while p or stack:
            while p:
                stack.append(p)
                p = p.left

            n = stack.pop()
            res.append(n.val)
            p = n.right

        return res
