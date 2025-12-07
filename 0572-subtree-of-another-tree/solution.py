# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(r, s):
            if not r and not s:
                return True
            if not r and s:
                return False
            if r and not s:
                return False
            if r.val != s.val:
                return False
            return isSame(r.left, s.left) and isSame(r.right, s.right)

        def isSub(root, subRoot):
            if root is None and subRoot is None:
                return True

            if root is None:
                return False

            if root.val == subRoot.val:
                if isSame(root, subRoot):
                    return True

            return isSub(root.left,subRoot) or isSub(root.right, subRoot)

        return isSub(root, subRoot)
