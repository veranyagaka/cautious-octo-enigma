1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
8
9        slow, fast = head, head
10
11        # fast moves 2x faster
12
13        while fast and fast.next:
14            slow = slow.next
15            fast = fast.next.next
16
17        return slow       
18        