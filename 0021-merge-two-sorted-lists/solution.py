# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node
        # Create pointer for both nodes
        # While both pointers are not None
        # Check which one is smaller and add to the dummy pointer and shift that pointer
        # Whichever node is not None add its values to the end of the linked list
        dummy = ListNode(0)
        p1 = list1
        p2 = list2
        d = dummy
        while p1 and p2:
            if p1.val < p2.val:
                d.next = ListNode(p1.val)
                p1 = p1.next
            else:
                d.next = ListNode(p2.val)
                p2 = p2.next
            d = d.next
        if p1 is not None:
            d.next = p1
        if p2 is not None:
            d.next = p2
        return dummy.next
