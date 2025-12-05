# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        stack = []
        p = root
        res = []

        while len(stack) != 0 or p:
            while p:
                stack.append(p)
                res.append(p.val)
                p = p.left

            n = stack.pop()
            p = n.right

        return res
