# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        q = deque([root])
        res = []
        while q:
            l = len(q)
            for i in range(l):
                if i == 0:
                    p = q.popleft()
                    res.append(p.val)
                else:
                    p = q.popleft()
                if p.right:
                    q.append(p.right)
                if p.left:
                    q.append(p.left)
        return res
