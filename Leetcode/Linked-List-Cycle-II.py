1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
9        # phase 1 and phase 2
10        # Floyd's cycle detection 
11        rabbit = head
12        tortoise = head
13       
14        while rabbit and rabbit.next:
15            rabbit = rabbit.next.next
16            tortoise = tortoise.next
17                # first intersection
18
19            if rabbit == tortoise:
20                break
21
22        if not rabbit or not rabbit.next:
23            return None
24                
25        ## phase 2
26
27        tortoise = head
28
29        while rabbit != tortoise: # second intersection
30            rabbit = rabbit.next
31            tortoise = tortoise.next
32
33        return tortoise
34
35