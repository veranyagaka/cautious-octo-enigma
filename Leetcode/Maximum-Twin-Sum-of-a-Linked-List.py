1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def pairSum(self, head: Optional[ListNode]) -> int:
8
9        slow, fast = head, head
10
11        while fast and fast.next:
12            slow = slow.next
13            fast = fast.next.next
14
15        middle = slow # the middle of the list
16
17        # reverse the second list: recall how to reverse a linked list
18        curr = middle
19        prev = None
20        
21        while curr:
22            next_node = curr.next
23            curr.next = prev
24            prev = curr
25
26            curr = next_node
27
28
29        first = head
30        max_sum = 0
31
32        while prev:
33
34            curr_sum = first.val + prev.val
35            first = first.next
36            prev = prev.next
37            if curr_sum > max_sum:
38                max_sum = curr_sum
39   
40        return max_sum
41        
42        """
43        hints
44        half the linked listst
45        find the middle using the fast and the slow pointers
46        traverse 2 lists at the same time and keep track of the max
47        """