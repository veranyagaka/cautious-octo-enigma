1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        # dummy = ListNode(-1) # no need for dummy ig
9        # no need for set if duplicate values are next to each other
10        curr = head
11
12        while curr and curr.next:
13            if curr.val == curr.next.val:
14                curr.next = curr.next.next # deleting a node
15            else:
16                curr = curr.next
17
18        return head
19        """
20        keep a set
21        how to do sorting .... the list is already sorted
22        """