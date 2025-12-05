# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q = deque([root])
        res = 0
        while q:
            l = len(q)
            for i in range(l):
                n = q.popleft()
                if n.right:
                    q.append(n.right)
                if n.left:
                    q.append(n.left)

            res += 1

        return res
