1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
8        dummy = ListNode()
9        curr = dummy
10
11        while list1 and list2:
12            if list1.val <= list2.val:
13                curr.next = list1
14                list1 = list1.next
15
16            else:
17                curr.next = list2
18                list2 = list2.next
19
20            curr = curr.next
21
22        curr.next = list1 or list2 # the remaining nodes
23
24        return dummy.next
25        