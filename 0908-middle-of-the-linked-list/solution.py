# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        p = head
        while p:
            res.append(p)
            p = p.next

        index = len(res)//2
        return res[index]
