# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        duplicate = set()
        while head:
            if head in duplicate:
                return True
            duplicate.add(head)
            head = head.next
        return False