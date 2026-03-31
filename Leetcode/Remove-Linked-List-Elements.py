1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
8        dummy = ListNode(0)
9        dummy.next = head
10
11        curr = head
12        prev = dummy
13
14        while curr:
15            if curr.val == val:
16                prev.next = curr.next # remove
17
18            else:
19                prev = curr
20
21            curr = curr.next
22            
23        return dummy.next
24        