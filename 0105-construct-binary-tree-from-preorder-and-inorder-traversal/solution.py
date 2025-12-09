# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def rec(pre, ino):
            if not pre or not ino:
                return None

            node = TreeNode(pre[0])
            position = ino.index(pre[0])
            node.left = rec(pre[1:position+1], ino[:position])
            node.right = rec(pre[position+1:], ino[position+1:])
            return node

        return rec(preorder, inorder)
        
