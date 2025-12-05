# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        res = []
        stack = []
        p = root

        while p or stack:
            while p:
                stack.append((p, False))
                p = p.left

            n = stack.pop()
            if n[1] == False:
                p = n[0].right
                stack.append((n[0], True))
            else:
                res.append(n[0].val)

        return res
