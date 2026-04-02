1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def hasCycle(self, head: Optional[ListNode]) -> bool:
9        
10        ## 
11        slow, fast = head, head
12
13        while fast and fast.next:
14            slow = slow.next
15            fast = fast.next.next
16
17            if fast == slow:
18                return True
19
20        return False