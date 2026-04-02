1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def isPalindrome(self, head: Optional[ListNode]) -> bool:
8        stack = []
9        curr = head
10        while curr:
11            stack.append(curr.val)
12            curr = curr.next
13
14        while head:
15            if head.val != stack.pop():
16                return False
17            head = head.next
18
19        return True