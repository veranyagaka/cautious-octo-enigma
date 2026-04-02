1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
8        ## neetcode help
9
10        # get
11        dummy = ListNode(-99, head)
12        leftPrev, curr = dummy, head # leftprev is the node just before left
13
14        for _ in range(left - 1):
15            leftPrev = leftPrev.next
16            curr = curr.next
17
18        # reverse
19        prev = None
20
21        for _ in range(right - left + 1): # 2-> 3-> 4 reversal
22            tmpNext = curr.next
23            curr.next = prev
24            prev, curr = curr, tmpNext
25
26        ## update the last 2 connections via the pointers
27        leftPrev.next.next = curr # 2 connecting to 5
28        leftPrev.next = prev # 1 connecting to 4
29        
30        return dummy.next