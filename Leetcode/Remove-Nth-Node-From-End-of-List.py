1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
8        ## two pointers
9        dummy = ListNode(-99, head)
10        fast = dummy
11        slow = dummy
12
13        for _ in range(n+1):
14            fast = fast.next
15
16        while fast:
17            slow = slow.next
18            fast = fast.next
19            
20        slow.next = slow.next.next
21
22        return dummy.next
23
24        
25        