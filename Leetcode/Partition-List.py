1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
8        ## split left and right then connect them at the end
9
10        left = ListNode(-1)
11        right = ListNode(-1)
12
13        first = left
14        right_pointer = right
15        curr = head
16
17        while curr:
18            #print(curr.val)
19            if curr.val < x:
20                left.next = curr
21                left = left.next
22            else:
23                right.next = curr
24                right = right.next
25
26            curr = curr.next
27
28        ## connect the left tail with the right head
29        #print(left)
30        #print(right)
31        # print(right_pointer)
32
33        left.next = right_pointer.next
34        right.next = None # 5 to none
35
36        return first.next
37