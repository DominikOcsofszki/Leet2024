# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list2:
            return list1
        if not list1:
            return list2
        start = ListNode()
        pointer = start
        while list1 and list2:
            if list1.val < list2.val:
                pointer.next = list1
                list1 = list1.next
            else:
                pointer.next = list2
                list2 = list2.next
            pointer = pointer.next
        pointer.next = list1 or list2
        return start.next
node1 = ListNode(1,ListNode(2,ListNode(3)))
node2 = ListNode(1,ListNode(3,ListNode(4)))
res = Solution().mergeTwoLists(node1,node2)
pointer = res
while pointer:
    print(pointer.val)
    pointer = pointer.next
